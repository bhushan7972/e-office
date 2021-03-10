from django.shortcuts import render, redirect
from .models import employeeP,employee_leave
from .forms import employee_profile,employee_leave_form,apply_job_Form
from django.contrib.auth.decorators import user_passes_test, login_required
from manager.models import Post,managerP,postcomment
from manager.forms import postcommentForm
from .models import CustomUser
from HR.models import Opening

from django.db.models import Q
# Create your views here.
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_employee, login_url='moderator:index')
def create_profile(request):

    employee = employeeP.objects.get(user=request.user)

    if request.method == 'POST':

        form = employee_profile(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('employee:dashboard')

    else:
        form = employee_profile()

    return render(request, 'employee/profile/create_profile.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_employee, login_url='moderator:index')
def dashboard(request):
    section='dashboard'
    # e_s = employeeP.objects.filter(department='SALES')
    # e_m = employeeP.objects.filter(department='MARKETING')
    # e_p = employeeP.objects.filter(department='PRODUCTION')
    # e_hr = employeeP.objects.filter(department='HR')
    # post3=Post.objects.all()
    post3  = Post.objects.all().order_by('-id')[:3]
    return render(request, 'employee/dashboard.html', locals())

def employee_leave(request):
    section = 'LeaveApplication'
    if request.method == 'POST':
        form = employee_leave_form(request.POST)
        employee = employeeP.objects.filter(user=request.user)[0]
        if form.is_valid():
            user = form.save(commit=False)
            user.employee_name = employee
            user.save()
            return render(request, 'employee/dashboard.html', locals())
    else:
        form = employee_leave_form()
        return render(request, 'employee/leave/employee_leave.html', locals())


def employee_viewpost(request):
    section = 'ViewPost'
    employee = employeeP.objects.get(user=request.user)
    print(employee.department)
    dict = []
    post1 = Post.objects.all()
    for i in post1:
        dept = i.author.department
        print(dept)
        if employee.department == dept:
            print(employee.department == dept)
            dict.append(i)
    print(dict)
    return render(request, 'employee/post/employee_viewpost.html', locals())

def employee_post_details(request,id):
    post2=Post.objects.filter(id=id)
    return render(request, 'employee/post/employee_post_details.html', locals())

def employee_post_comment(request,id):
    
    if request.method == "POST":
        form=postcommentForm(request.POST)
        post= Post.objects.get(id=id)
        author=CustomUser.objects.get(id=request.user.id)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.sender=author
            comment.save()
            emp1 = Post.objects.filter(id=id)
            emp = CustomUser.objects.filter(id=id)
            comments = postcomment.objects.filter(post=post)
       # return render(request, 'manager/post/commentform.html', locals())
       # return redirect('employee:dashboard')

            show_comment = postcomment.objects.all().order_by('-id')[:1]
        return render(request, 'employee/post/employee_show_postcomment.html', locals())

    else:
        form=postcommentForm()
        return render(request, 'employee/post/employee_post_comment.html', locals())

def my_profile(request):
    post4 = Post.objects.all().order_by('-id')[:2]
    emp = employeeP.objects.filter(user=request.user)[0]
    return render(request, 'employee/profile/my_profile.html',locals())

def edit_profile(request):
    emp1 = employeeP.objects.get(user=request.user)
    if request.method == 'POST':
        form = employee_profile(request.POST, request.FILES,instance=emp1)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'employee/dashboard.html', locals())
    else:
        form = employee_profile(instance=emp1)
        return render(request, 'employee/profile/edit_profile.html', locals())


def apply_job(request,id):
    print(f"hii{id}")
    if request.method == 'POST':
        form = apply_job_Form(request.POST,request.FILES)
        title = Opening.objects.filter(id=id)[0]
        if form.is_valid():
            print("Welocme to job form")
            user = form.save(commit=False)
            user.job_title = title
            user.save()
            allopenings = Opening.objects.all()
            return render(request, 'hr/homeopenings/homeopen.html', locals())
    else:
        form = apply_job_Form()
        return render(request,'employee/current_opening/apply_job.html',locals())

def search_posting(request):
    search_postings = request.GET.get('search')
    job_postings = []
    postings = Opening.objects.filter(Q(designation__icontains=search_postings))
    for i in postings:
       job_postings.append(i)
    return render(request, 'employee/current_opening/search_posting.html', locals())



