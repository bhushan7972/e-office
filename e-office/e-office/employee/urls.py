from django.urls import path
from .views import create_profile, dashboard,employee_leave,employee_viewpost,employee_post_details,employee_post_comment,my_profile,edit_profile
from .views import apply_job,search_posting
app_name = 'employee'

urlpatterns = [
         ############  Profile Related ##########
    path('createprofile', create_profile, name = 'createprofile'),
    path('my_profile', my_profile, name='my_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
         ############  Dashboard Related ##########
    path('dashboard', dashboard, name = 'dashboard'),
        ############  Leave Related ##########
    path('employee_leave', employee_leave, name = 'employee_leave'),
        ############  Post Related ##########
    path('employee_viewpost', employee_viewpost, name = 'employee_viewpost'),
    path('employee_post_details/<int:id>', employee_post_details, name = 'employee_post_details'),
    path('employee_post_comment/<int:id>', employee_post_comment, name = 'employee_post_comment'),
        ############  Jobs-openings Related ##########

    path('apply_job/<int:id>',apply_job,name='apply_job'),
    path('search_posting/',search_posting,name='search_posting'),

]