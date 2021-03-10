from django.urls import path
from .views import task_detail_view,create_profile,attendence_detail_view,close_task_desc, dashboard,create_post,post1,view_employee_leave,manager_leave,detail_leave_application
from .views import updateprofile,leave_application_status,attendence_record,task_close_form,task_close,close_task,view_profile,detail_post_application,viewstaff,postComment,commentform,search,createtask,upcoming_task,active_task
from .views import Mark_attendence_record,Mark_attendence,today_employee_onworking,view_profile2
app_name = 'manager'

urlpatterns = [

    path('createprofile/', create_profile, name = 'createprofile'),
    path('updateprofile/', updateprofile, name='updateprofile'),
    path('view_profile/', view_profile, name='view_profile'),
    path('createpost/', create_post, name = 'createpost'),
    path('view_profile2/<int:id>', view_profile2, name = 'view_profile2'),


    path('dashboard/', dashboard, name='dashboard'),
    path('post/', post1, name='post'),
    path('detail_post_application/<int:id>', detail_post_application, name='detail_post_application'),
    path('view_employee_leave', view_employee_leave, name='view_employee_leave'),

    path('manager_leave', manager_leave, name='manager_leave'),
    path('detail_leave_application/<int:id>', detail_leave_application, name='detail_leave_application'),
    path('leave_application_status/<int:id>', leave_application_status, name='leave_application_status'),
    path('viewstaff', viewstaff, name='viewstaff'),

    path('commentform/<int:id>',commentform, name="commentform"),

    path('postComment/<int:id>', postComment, name="postComment"),
    path('search/', search, name="search"),
    path('createtask/', createtask, name = 'createtask'),
    path('upcoming_task/', upcoming_task, name = 'upcoming_task'),
    path('active_task/', active_task, name = 'active_task'),
    path('close_task/<int:id>', close_task, name = 'close_task'),

    path('task_detail_view/<int:id>', task_detail_view, name = 'task_detail_view'),
    path('task_close_form/<int:id>', task_close_form, name = 'task_close_form'),
    path('task_close/', task_close, name = 'task_close'),
    path('close_task_desc/<int:id>', close_task_desc, name = 'close_task_desc'),


    path('attendence_record/', attendence_record, name = 'attendence_record'),
    path('Mark_attendence_record/', Mark_attendence_record, name = 'Mark_attendence_record'),
    path('Mark_attendence/<int:id>', Mark_attendence, name = 'Mark_attendence'),
    path('attendence_detail_view/<int:id>', attendence_detail_view, name = 'attendence_detail_view'),
    path('today_employee_onworking/', today_employee_onworking, name = 'today_employee_onworking'),



]