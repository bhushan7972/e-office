from django.urls import path
from .views import create_profile, dashboard,create_post,post1,manager_leave,view_employee_leave

app_name = 'manager'

urlpatterns = [

    path('createprofile/', create_profile, name = 'createprofile'),
    path('createpost/', create_post, name = 'createpost'),

    path('dashboard/', dashboard, name='dashboard'),
    path('post/', post1, name='post'),

    path('manager_leave',manager_leave, name = 'manager_leave'),
    path('view_employee_leave',view_employee_leave, name = 'view_employee_leave'),

]