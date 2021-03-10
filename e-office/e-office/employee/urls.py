from django.urls import path
from .views import create_profile, dashboard,employee_leave

app_name = 'employee'

urlpatterns = [

    path('createprofile', create_profile, name = 'createprofile'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('employee_leave', employee_leave, name = 'employee_leave'),

]