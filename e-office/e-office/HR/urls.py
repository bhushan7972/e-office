from django.urls import path
from .views import hrProfile, dashboard,sep_dashboard


app_name = 'hr'

urlpatterns = [

    path('createprofile', hrProfile, name = 'createprofile'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('sep_dashboard:<str:depart>', sep_dashboard, name ='sep_dashboard'),
]