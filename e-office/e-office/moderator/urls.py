from django.urls import path
from .views import CreateProfile, sent, signup_manager, signup_hr, signup_employee, index, signup_modertor, dashboard, production, marketing, hr_dep, sales, active_tasks, closed_tasks, upcoming_tasks, notify, write_post, hr, manager, employee, view_profile,updateprofile, notification_detail, notification_list, notifyform, staff_search, message, list_msg, msg_detail 

app_name = 'moderator'

urlpatterns = [
    path('signup_manager/', signup_manager, name='signup_manager'),
    path('signup_hr/', signup_hr, name='signup_hr'),
    path('signup_employee/', signup_employee, name='signup_employee'),
    path('signup_moderator/', signup_modertor),

    path('index/', index, name='index'),

    path('dashboard/', dashboard, name='dashboard'),

    # Profile related
    path('createprofile/', CreateProfile, name='createprofile'),
    path('updateprofile/', updateprofile, name='updateprofile'),
    path('view_profile/', view_profile, name='view_profile'),

    # Departments
    path('marketing/', marketing, name='marketing'),
    path('production/', production, name='production'),
    path('hr_dep/', hr_dep, name='hr_dep'),
    path('sales/', sales, name='sales'),

    # Tasks
    path('active_tasks/', active_tasks, name='active_tasks'),
    path('closed_tasks/', closed_tasks, name='closed_tasks'),
    path('upcoming_tasks/', upcoming_tasks, name='upcoming_tasks'),

    # Write
    path('notify/', notify, name='notify'),
    path('write_post/', write_post, name='write_post'),

    # Staff
    path('hr/', hr, name='hr'),
    path('manager/', manager, name='manager'),
    path('employee/', employee, name='employee'),

    # Notification
    path('notifyform/', notifyform, name='notifyform'),
    path('notification_list/', notification_list, name='notification_list'),
    path('notification_detail/<int:id>', notification_detail, name='notification_detail'),
    path('sent/', sent, name='sent'),

    # Notification
    path('message/<int:id>', message, name='message'),
    path('list_msg/', list_msg, name='list_msg'),
    path('msg_detail/<int:id>', msg_detail, name='msg_detail'),

    # Search
    path('search/', staff_search, name='staff_search'),
]