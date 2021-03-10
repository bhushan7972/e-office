from django.urls import path
from .views import hrProfile,vew_pro,viewopenings,dashboard,sep_dashboard,leave_application,Posts,leave_details,post_details,openings,search,view_my_pro,job_details


app_name = 'hr'

urlpatterns = [

    path('createprofile', hrProfile, name = 'createprofile'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('sep_dashboard:<str:depart>', sep_dashboard, name ='sep_dashboard'),

    path('leave_application', leave_application, name ='leave_application'),
    path('leave_details:<int:per_id>', leave_details, name='leave_details'),

    path('Posts', Posts, name='Posts'),
    path('post_details:<int:per_id>', post_details, name='post_details'),

    path('openings', openings, name='openings'),
    path('viewopenings', viewopenings, name='viewopenings'),
    path('job_details:<int:id>', job_details, name='job_details'),

    path('search', search, name='search'),

    path('vew_pro:<int:id>', vew_pro, name='vew_pro'),
    path('my_profile/',view_my_pro, name='view_my_pro'),

]