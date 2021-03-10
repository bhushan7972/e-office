from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomUserCreationForm, profile, form, storage, message_form, msg_storage
from .models import Profile, notifications, store, CustomUser, messages, store_msg
from django.contrib.auth import login, authenticate
from manager.models import managerP
from HR.models import hrP
from employee.models import employeeP
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='/')
def index(request):

    if request.user.is_hr:
        hr = hrP.objects.get(user=request.user)
        if hr.is_active:
            return redirect('hr:dashboard')    
        else:
            return redirect('hr:createprofile')   
              
    if request.user.is_employee:
        employee = employeeP.objects.get(user=request.user)
        if employee.is_active:
            return redirect('employee:dashboard')    
        else:
            return redirect('employee:createprofile')   

    if request.user.is_manager:
        manager = managerP.objects.get(user=request.user)
        if manager.is_active:
            return redirect('manager:dashboard')

        else:
            return redirect('manager:createprofile')    
    
    if request.user.is_moderator:
        moderator = Profile.objects.get(user=request.user)
        if moderator.is_active:
            return redirect('moderator:dashboard')    
        else:
            return redirect('moderator:createprofile')     

    return render(request, 'moderator/index.html')        

# Create your views here.

def signup_manager(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_manager = True
            user.save()
            manager = managerP.objects.create(user=user)
            # messages.success(request, 'Your Account has been created successfull!')
            login(request, user)
            return redirect('manager:createprofile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/manager_signup.html', locals())


def signup_hr(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_hr = True
            user.save()
            hr = hrP.objects.create(user=user)
            # messages.success(request, 'Your Account has been created successfull!')
            login(request, user)
            return redirect('hr:createprofile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/hr_signup.html', locals())


def signup_employee(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.save()
            employee = employeeP.objects.create(user=user)
            # messages.success(request, 'Your Account has been created successfull!')
            login(request, user)
            return redirect('employee:createprofile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/employee_signup.html', locals())

def signup_modertor(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_moderator = True
            user.save()
            moderator = Profile.objects.create(user=user)
            # messages.success(request, 'Your Account has been created successfull!')
            login(request, user)
            return redirect('moderator:createprofile')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/moderator_signup.html', locals())

# Profile related
@login_required(redirect_field_name='/')
def CreateProfile(request):

    moderator = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        form = profile(request.POST, request.FILES, instance=moderator)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('moderator:dashboard')
    else:
        form = profile()

    return render(request, 'moderator/profile/create_profile.html', locals()) 

@login_required(redirect_field_name='/')
def updateprofile(request):

    moderator = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = profile(request.POST, request.FILES, instance=moderator)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('moderator:view_profile')
    else:
        form = profile(instance=moderator)   
    return render(request, 'moderator/profile/update_profile.html', locals())

   
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def view_profile(request):
    return render(request, 'moderator/profile/view_profile.html', locals())               



@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def dashboard(request):

    user = CustomUser.objects.all()
     
    section='dashboard' 
    return render(request, 'moderator/dashboard.html', locals())




# Departments
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def production(request):
    section = 'department'
    return render(request, 'moderator/departments/production.html', locals())   

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def marketing(request):
    section = 'department'
    return render(request, 'moderator/departments/marketing.html', locals()) 

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def hr_dep(request):
    section = 'department'
    return render(request, 'moderator/departments/hr.html', locals()) 

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def sales(request):
    section = 'department'
    return render(request, 'moderator/departments/sales.html', locals())   


# Tasks
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def active_tasks(request):
    section = 'tasks'
    return render(request, 'moderator/tasks/active_tasks.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def closed_tasks(request):
    section = 'tasks'
    return render(request, 'moderator/tasks/closed_tasks.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def upcoming_tasks(request):
    section = 'tasks'
    return render(request, 'moderator/tasks/upcoming_tasks.html', locals())


# Write
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def notify(request):
    section = 'write'
    return render(request, 'moderator/write/notify.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def write_post(request):
    section = 'write'
    return render(request, 'moderator/write/post.html', locals())


# Staff
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def hr(request):
    section = 'staff'
    return render(request, 'moderator/staff/hr.html', locals())    

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')    
def manager(request):
    section = 'staff'
    return render(request, 'moderator/staff/manager.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def employee(request):
    section = 'staff'
    return render(request, 'moderator/staff/employee.html', locals()) 

# Search
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def staff_search(request):
    section = 'staff_search'
    return render(request, 'moderator/staff/find.html', locals())



# For Notifications
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def notifyform(request):
    # noti = notifications.objects.all()

    # stored = store.objects.all()

    if request.method == 'POST':
        form1 = form(request.POST)
        if form.is_valid:
            notice = form1.save(commit=False)
            if request.user.is_moderator:
                notice.sender = 'Admin'
            if request.user.is_hr:
                notice.sender = 'HR'    
            notice.save()
            for i in CustomUser.objects.all():
                storedm = storage()
                st = storedm.save(commit=False)
                st.notification_id = notice.id
                st.sn = i.id
                st.save()
            return redirect('moderator:sent')    
                
    else:
        form1 = form()        
    
    section = 'write'
    return render(request, 'moderator/notifications/write.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_moderator, login_url='moderator:index')
def sent(request):
    section = 'write'
    return render(request, 'moderator/notifications/sent.html',locals())


# def new_notification(request):

#     storedmsg = []
#     stored = store.objects.filter(sn=request.user.id)   
#     for i in stored:
#         storedmsg.append(i.title)             

#     section = 'write'
#     return render(request, 'layouts/base_dashboard.html', locals())    

@login_required(redirect_field_name='/')
def notification_list(request):

    noti = notifications.objects.all()
    storedmsg = []
    stored = store.objects.filter(sn=request.user.id)   
    for i in stored:
        storedmsg.append(i.notification_id)     
    
    section = 'write'
    return render(request, 'moderator/notifications/view.html', locals()) 

@login_required(redirect_field_name='/')
def notification_detail(request,id):

    notice = notifications.objects.get(id=id)

    try:
        store.objects.get(notification_id=id,sn=request.user.id).delete()
    except:
        pass    
    
    section = 'write'
    return render(request, 'moderator/notifications/detail.html', locals())

# For messages
@login_required(redirect_field_name='/')
def message(request,id):

    sender = CustomUser.objects.get(id=request.user.id)
    receiver = CustomUser.objects.get(id=id)

    if request.method == 'POST':
        form = message_form(request.POST)
        if form.is_valid:
            mg = form.save(commit=False)
            mg.sender = sender
            mg.receivar = receiver
            mg.save()
            
            
            storedm = msg_storage()
            st = storedm.save(commit=False)
            st.msg_id = mg.id
            st.sn = id
            st.save()
            return redirect('moderator:sent')    

    else:
        form = message_form()

    return render(request,'moderator/messages/write.html', locals())    


@login_required(redirect_field_name='/')
def list_msg(request):

    msg = messages.objects.filter(receivar=request.user)
    storedmsg = []
    stored = store_msg.objects.filter(sn=request.user.id)   
    for i in stored:
        storedmsg.append(i.msg_id)     
    
    return render(request, 'moderator/messages/view.html', locals()) 

@login_required(redirect_field_name='/')
def msg_detail(request, id):

    msg = messages.objects.get(id=id)

    try:
        store_msg.objects.get(msg_id=id,sn=request.user.id).delete()
    except:
        pass    

    return render(request, 'moderator/messages/detail.html', locals())