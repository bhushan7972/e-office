from django.shortcuts import render, redirect
from .models import employeeP,employee_leave
from .forms import employee_profile,employee_leave_form
from django.contrib.auth.decorators import user_passes_test, login_required

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
    e_s = employeeP.objects.filter(department='SALES')
    e_m = employeeP.objects.filter(department='MARKETING')
    e_p = employeeP.objects.filter(department='PRODUCTION')
    e_hr = employeeP.objects.filter(department='HR')
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
        return render(request, 'employee/leave/manager_leave.html', locals())




      