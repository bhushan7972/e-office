from django.shortcuts import render, redirect
from .models import managerP
from .models import Post
from .forms import manager_profile,manager_leave_form,postForm
from employee.models import employeeP,employee_leave

from .forms import postForm
from django.contrib.auth.decorators import user_passes_test, login_required


# Create your views here.
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='moderator:index')
def create_profile(request):

    manager = managerP.objects.get(user = request.user)

    if request.method == 'POST':

        form = manager_profile(request.POST, request.FILES, instance=manager)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('manager:dashboard')
    else:
        form = manager_profile()

    return render(request, 'manager/profile/create_profile.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='moderator:index')
def dashboard(request):
    section='dashboard'
    emp = managerP.objects.all()
    return render(request, 'manager/dashboard.html', locals())

def create_post(request):
    emp = Post.objects.all()

    manager = managerP.objects.filter(user=request.user)[0]

    if request.method == 'POST':
        form = postForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.author = manager
            user.save()

            return redirect('manager:dashboard')
    else:
        form = postForm()
    section = 'write'
    return render(request, 'manager/post/create_post.html', locals())



def post1(request):
    manager = managerP.objects.filter(user=request.user)[0]
    print(manager.department)

   # department=managerP.objects.filter(department=manager.department)
    emp = Post.objects.filter(author=manager)
   # emp=Post.objects.filter(author=department)
    print(emp)
    section='write'
    return render(request, 'manager/post/post.html', locals())


def manager_leave(request):
    section = 'LeaveApplication'
    if request.method == 'POST':
        form = manager_leave_form(request.POST)
        manager = managerP.objects.filter(user=request.user)[0]
        if form.is_valid():
            user = form.save(commit=False)
            user.manager_name = manager
            user.save()
            return render(request, 'manager/dashboard.html', locals())
    else:
        form = manager_leave_form()
        return render(request, 'manager/leave/manager_leave.html', locals())

def view_employee_leave(request):
    empl_onleave=employee_leave.objects.all()
    return render(request,'manager/leave/view_employee_leave.html',locals())
