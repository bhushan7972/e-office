from django import forms
from .models import employeeP,employee_leave,job_apply
from moderator.choices import *

import datetime
from datetime import datetime, time, date, timedelta
min_date = date.today() - timedelta(50*365)
today = date.today() - timedelta(18*365)



class employee_profile(forms.ModelForm):

    maritial_status = forms.ChoiceField(choices=maritial_status,widget=forms.RadioSelect,required=True)
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect,required=True)

    class Meta:
        model = employeeP
        fields = '__all__'
        exclude = ['user','is_active' ]

class employee_leave_form(forms.ModelForm):
    leave_from_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'value': today, 'type': 'date'}),
                                 )
    leave_to_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                    'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = employee_leave
        fields = '__all__'   
        exclude= ['employee_name','work_status']

class apply_job_Form(forms.ModelForm):
    birthdate = forms.DateField(required=False,widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'value': today, 'type': 'date'}),
                                 )
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect,required=True)

    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    email = forms.CharField(required=False)
    mobileno = forms.IntegerField(required=False)

    Qualification = forms.CharField(required=False)

    yearofpassing = forms.IntegerField(required=False)
    yearofexperience = forms.FloatField(required=False)
    resume = forms.FileField(required=False)

    class Meta:
        model = job_apply
        fields = '__all__'
        exclude= ['job_title']
