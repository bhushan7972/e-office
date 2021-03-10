from django.shortcuts import render, redirect
from .models import managerP,attendence
from .models import Post
from HR.models import hrP
from .models import postcomment,task
from .forms import manager_profile,manager_leave_form,taskForm,closetaskForm
from .forms import postForm,postcommentForm,AttendenceForm
from django.contrib.auth.decorators import user_passes_test, login_required
from employee.models import employeeP,employee_leave
from employee.forms import employee_leave_form
from moderator.models import CustomUser
from django.db.models import Q
from django.db.models import F
from datetime import date
from datetime import datetime
from django.utils.timezone import now

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


@login_required(redirect_field_name='/')
def updateprofile(request):
    manager = managerP.objects.get(user=request.user)

    if request.method == 'POST':
        form = managerP(request.POST, request.FILES, instance=manager)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('manager:view_profile')
    else:
        form = manager_profile(instance=manager)
    return render(request, 'manager/profile/update_profile.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='manager:index')
def view_profile(request):
    data=managerP.objects.filter( user_id=request.user.id)
    print(data)
    return render(request, 'manager/profile/view_profile.html', locals())


def create_post(request):
    section = 'Write'
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

    return render(request, 'manager/post/create_post.html', locals())

def post1(request):
    section = 'viewpost'
    manager = managerP.objects.filter(user=request.user)[0]
    print(manager.department)

   # department=managerP.objects.filter(department=manager.department)
    emp = Post.objects.filter(author=manager)
   # emp=Post.objects.filter(author=department)
    return render(request, 'manager/post/post.html', locals())


def detail_post_application(request,id):
   # department=managerP.objects.filter(department=manager.department)
    #emp1 = Post.objects.filter(id=id)
    emp1 = Post.objects.filter(id=id)
    emp = CustomUser.objects.filter(id=id)
    post=Post.objects.get(id=id)
    comments = postcomment.objects.filter(post=post)
    a=len(comments)
    # emp=Post.objects.filter(author=department)
    return render(request, 'manager/post/detail_post_application.html', locals())

def view_employee_leave(request):
    section='leave'

    empl_onleave=employee_leave.objects.all()
    return render(request,'manager/leave/view_employee_leave.html',locals())

def manager_leave(request):
    section='leave'
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

def detail_leave_application(request,id):
    emp_data = employee_leave.objects.filter(id=id)
    return render(request, 'manager/leave/detail_leave_application.html', locals())

def leave_application_status(request,id):
    leavestatus = request.POST.get('leavestatus', '')
    print(leavestatus)
    emp_data = employee_leave.objects.filter(id=id).update(work_status=leavestatus)
    return render(request, 'manager/dashboard.html', locals())


def viewstaff(request):
    section='viewstaff'
    emp = employeeP.objects.all()
    return render(request, 'manager/staff/viewstaff.html', locals())


from django.contrib import messages



def postComment(request,id):
    if request.method == "POST":
        form=postcommentForm(request.POST)
        post= Post.objects.get(id=id)
        author=CustomUser.objects.get(id=request.user.id)
        print(form,post,author)
        if form.is_valid():

            comment=form.save(commit=False)
            comment.post=post
            comment.sender=author
            comment.save()
            #emp = Post.objects.filter(id=id)
            emp = CustomUser.objects.filter(id=id)
            emp1 = Post.objects.filter(id=id)
            comments = postcomment.objects.filter(post=post)
            a = len(comments)
        return render(request, 'manager/post/detail_post_application.html', locals())
    else:
        form=postcommentForm()
        return render(request, 'manager/post/comment_form.html', locals())

def commentform(request,id):
    form = postcommentForm()
    emp1 = Post.objects.filter(id=id)

    return render(request,'manager/post/comment_form.html', locals())

def search(request):
    section = 'FindStaff'
    result = CustomUser.objects.all()
    search_query = request.GET.get('search')
    print(search_query)
    if search_query:
        for data in search_query.split():
            results = CustomUser.objects.filter(Q(first_name__icontains=data) | Q(last_name__icontains=data))
            employee_list = []

            for i in results:
                if i.is_employee:
                    employees = employeeP.objects.get(user=i)
                    employee_list.append(employees)
            return render(request, 'manager/search/search_result.html', locals())
    return render(request, 'manager/search/searchform.html', locals())

def createtask(request):
    section='Write'
    if request.method == "POST":
        form=taskForm(request.POST,request.FILES)
        task_assign_By=CustomUser.objects.get(id=request.user.id)
        taskassigndate=request.POST.get('task_assign_date')
        print(taskassigndate)

        print(form)
        if form.is_valid():
            print('data get')
            taskform=form.save(commit=False)

            taskform.task_assign_By=task_assign_By

            taskform.save()

            return render(request, 'manager/dashboard.html', locals())
        else:
            return render(request, 'manager/dashboard.html', locals())
    else:
        form = taskForm()
        return render(request, 'manager/task/task_form.html', locals())

def upcoming_task(request):
    section = 'task'
    task_data=task.objects.filter(Q( task_assign_date__gt=date.today()) & Q(task_status='Waiting Aprove'))
    return render(request, 'manager/task/upcoming_task.html', locals())

def active_task(request):
    section='task'
    task_data2 = task.objects.filter(task_assign_date__lte=date.today())
    task_data2 = task.objects.filter(Q(task_assign_date__lte=date.today()) & Q(task_status='Waiting Aprove') ).update(task_status='Working')

    task_data=task.objects.filter(Q(task_assign_date__lte=date.today())& Q(task_status='Working'))
    return render(request,'manager/task/active_task.html', locals())

def task_detail_view(request,id):
    section = 'task'
    task_data= task.objects.filter(id=id)
    return render(request, 'manager/task/task_detail_view.html', locals())

def close_task(request,id):
    section = 'Write'
    if request.method == "POST":
        form = closetaskForm(request.POST,request.FILES)
        tasksta=request.POST.get('task_status','')
        disc=request.POST.get('close_task_descriptions','')
        task_assign_By = CustomUser.objects.get(id=request.user.id)
        if form.is_valid():
            datenow=datetime.today()
            taskform = form.save(commit=False)
            taskForm.task_status=tasksta
            taskform.task_assign_By = task_assign_By
            taskForm.close_task_descriptions=disc
            task_data2 = task.objects.filter(id=id).update(task_status=tasksta)
            task_data2 = task.objects.filter(id=id).update(close_task_descriptions=disc)
            task_data2 = task.objects.filter(id=id).update(close_task_date=datenow)
            return render(request, 'manager/dashboard.html', locals())
    return render(request, 'manager/dashboard.html', locals())

def task_close_form(request,id):
    a=id
    form = closetaskForm()
    return render(request, 'manager/task/close_task_form.html', locals())

def task_close(request):
    section = 'task'
    task_data = task.objects.filter(Q(task_status='Completed')|Q(task_status='Incomplete close'))
    return render(request, 'manager/task/close_task.html', locals())

def close_task_desc(request,id):
    section = 'task'
    task_data = task.objects.filter(id=id)
    return render(request, 'manager/task/close_task_description.html', locals())

def attendence_record(request):

    attendence_record_data=employeeP.objects.all()
    return render(request, 'manager/Attendence_record/attendence_record.html', locals())

def Mark_attendence_record(request):


    attendence_record_data = employeeP.objects.all()

    print(attendence_record_data)

    this_month_date = date.today()
    this_month_date = this_month_date.replace(day=1)

    emp_data = employee_leave.objects.filter(Q(leave_from_date__lte=date.today()) & Q(leave_from_date__gte=this_month_date))
    print(emp_data)

    a=[]
    for i in emp_data:
        a.append(i.employee_name)
    print(a)
    return render(request, 'manager/Attendence_record/mark_attendence.html', locals())

def Mark_attendence(request,id):
    a=id
    if request.method == "POST":
        form = AttendenceForm(request.POST)

        name = CustomUser.objects.get(id=id)
        data = employeeP.objects.get(Q(user=name))
        if form.is_valid():
            taskform = form.save(commit=False)
            taskform.emp_name=data

            taskform.save()
            attendence_record_data = employeeP.objects.all()

            return render(request, 'manager/Attendence_record/mark_attendence.html', locals())


    form = AttendenceForm()
    return render(request, 'manager/Attendence_record/mark_attendence_form.html', locals())


def attendence_detail_view(request,id):
    user_id=id
    month = request.POST.get('month')
    year = request.POST.get('year')
    name=CustomUser.objects.get(id = id)
    data=employeeP.objects.get(user=name)

    if request.method == "POST":
        pass
    form = AttendenceForm()
    attendence_record_data = attendence.objects.filter( Q(emp_name=data) & Q(select_month=month) )

    return render(request,'manager/Attendence_record/attendence_record_detail_view.html',locals())


def today_employee_onworking(request):
    this_month_date = date.today()

    this_month_date = this_month_date.replace(day=1)

    emp_data = employee_leave.objects.filter(Q(leave_from_date__lte=date.today()) & Q(leave_from_date__gte=this_month_date))
    return render(request, 'manager/Attendence_record/today_employee_work_status.html', locals())


def view_profile2(request,id):
    print(id)
    user_c = CustomUser.objects.get(id=id)
    print(user_c)
    if user_c.is_employee:
        per = employeeP.objects.filter(user=user_c)
        return render(request, 'hr/userprofile/uprofile.html', locals())
    if user_c.is_manager:
        per = managerP.objects.filter(user=user_c)
        return render(request, 'hr/userprofile/uprofile.html', locals())
    if user_c.is_hr:
        per = hrP.objects.filter(user=user_c)
        return render(request, 'hr/userprofile/uprofile.html', locals())