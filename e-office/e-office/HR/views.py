from django.shortcuts import render, redirect
from .forms import hr_profile
from .models import hrP
from manager.models import managerP
from employee.models import employeeP
from django.contrib.auth.decorators import user_passes_test, login_required


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
    hr = hrP.objects.filter(department = depart)
    manager = managerP.objects.filter(department = depart)
    employee = employeeP.objects.filter(department = depart)
    return render(request, 'hr/dep.html', locals()) 