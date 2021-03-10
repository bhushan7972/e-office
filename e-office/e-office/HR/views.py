from django.shortcuts import render, redirect
from .forms import hr_profile,openingform
from .models import hrP,Opening
from moderator.models import CustomUser,Profile
from manager.models import managerP,Post
from employee.models import employeeP,employee_leave
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse


# Create your views here.
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_hr, login_url='moderator:index')
def hrProfile(request):

    hr = hrP.objects.get(user=request.user)

    if request.method == 'POST':
        
        form = hr_profile(request.POST, request.FILES, instance=hr)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('hr:dashboard')
    else:
        form = hr_profile()

    return render(request, 'hr/profile/create_profile.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_hr, login_url='moderator:index')
def dashboard(request):
    section='dashboard'
    hr = hrP.objects.all()
    hr_pro = hrP.objects.filter(department='PRODUCTION')
    hr_sales = hrP.objects.filter(department='SALES')
    hr_marketing = hrP.objects.filter(department='MARKETING')
    hr_hr = hrP.objects.filter(department='HR')
    return render(request, 'hr/dashboard.html', locals()) 

def sep_dashboard(request,depart):
    section='department'
    manager = managerP.objects.filter(department = depart)
    employee = employeeP.objects.filter(department = depart)
    if depart == 'PRODUCTION':
        return render(request, 'hr/department/productiondep.html', locals()) 
    elif depart == 'MARKETING':
        return render(request, 'hr/department/marketingdep.html', locals())
    elif depart == 'SALES':  
        return render(request, 'hr/department/salesdep.html', locals())
    else:
        hr = hrP.objects.filter(department = depart)
        return render(request, 'hr/department/hrdep.html', locals())

def leave_application(request):
    section ='Leave Application'
    leave = employee_leave.objects.all()
    return render(request,'hr/leave/leave.html',locals())

def leave_details(request,per_id):
    section = 'Leave Application'
    per_user = CustomUser.objects.filter(id= per_id)[0]
    employee = employeeP.objects.filter(user=per_user)[0]
    leavedetails = employee_leave.objects.filter(employee_name=employee)
    return render(request, 'hr/leave/leave_details.html', locals())

def Posts(request):
    section = 'Posts'
    posts = Post.objects.all()
    return render(request,'hr/posts/posts.html',locals())

def post_details(request,per_id):
    section = 'Posts'
    per_user = CustomUser.objects.filter(id=per_id)[0]
    manager = managerP.objects.filter(user=per_user)[0]
    postdetails = Post.objects.filter(author=manager)
    return render(request, 'hr/posts/post_details.html', locals())

def openings(request):
    section = 'Carrier'
    hr = hrP.objects.get(user=request.user)
    if request.method == 'POST':
        form = openingform(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.hruser = hr
            forms.save()
            return render(request, 'hr/dashboard.html',locals()) 
    else:
        form=openingform()
        return render(request,'hr/openings/opening.html',locals())


def search(request):
    section ='Find Staff'
    result = CustomUser.objects.all()
    # print(f'the result is {result}')
    search_query = request.GET.get('search','')
    # print(search_query)
    if search_query:
        for term in search_query.split():
            results = CustomUser.objects.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
            employee_list = []
            manager_list = []
            hr_list = []
            for i in results :
                if i.is_employee:
                    employees = employeeP.objects.filter(user=i)[0]
                    employee_list.append(employees)
                if i.is_manager:
                    managers = managerP.objects.filter(user=i)[0]
                    manager_list.append(managers)
                if i.is_hr:
                    hr = hrP.objects.get(user=i)
                    hr_list.append(hr)
            # print(f'the result is {results}')
            return render(request,'hr/search/search.html',locals())
    return render(request,'hr/search/search.html',locals())


def viewopenings(request):
    allopenings = Opening.objects.all()
    return render(request,'hr/homeopenings/homeopen.html',locals())

def job_details(request,id):
    details = Opening.objects.filter(id=id)
    print(f"hii{details}")
    return render(request, 'hr/homeopenings/job_details.html', locals())


    #Reserved.objects.filter(client=client_id).order_by('-check_in')

def vew_pro(request,id):
    print(id)
    user_c = CustomUser.objects.get(id=id)
    print(user_c)
    if user_c.is_employee:
        per = employeeP.objects.filter(user=user_c)
        return render(request,'hr/userprofile/uprofile.html',locals()) 
    if user_c.is_manager:
        per = managerP.objects.filter(user=user_c)
        return render(request,'hr/userprofile/uprofile.html',locals()) 
    if user_c.is_hr:
        per = hrP.objects.filter(user=user_c)
        return render(request,'hr/userprofile/uprofile.html',locals()) 

def view_my_pro(request):
    pro = hrP.objects.get(user=request.user)
    hr = hrP.objects.get(user=request.user)
    return render(request,'hr/profile/my_profile.html',locals())