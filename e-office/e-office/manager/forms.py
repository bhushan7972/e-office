from django import forms
from .models import managerP,manger_leave,task,attendence
from .models import Post,postcomment
from moderator.choices import *
from datetime import datetime, time, date, timedelta
min_date = date.today() - timedelta(50*365)
today = date.today() - timedelta(18*365)



class manager_profile(forms.ModelForm):

    maritial_status = forms.ChoiceField(choices=maritial_status,widget=forms.RadioSelect,required=True)
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect,required=True)

    class Meta:
        model = managerP
        fields = '__all__'
        exclude = ['user','is_active' ]

class postcommentForm(forms.ModelForm):

    class Meta:
        model = postcomment
        fields = '__all__'
        exclude =['sender','post']

class postForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['author','post_date']

class manager_leave_form(forms.ModelForm):
    leave_from_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                    'value': today, 'type': 'date'}),
                                 )
    leave_to_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = manger_leave
        fields = '__all__'
        exclude= ['manager_name']

class taskForm(forms.ModelForm):
    task_assign_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                                 attrs={'class': 'form-control datepicker',
                                                                        'min': min_date
                                                                        , 'value': today, 'type': 'date'}),
                                     )


    class Meta:
        model = task
        fields = "__all__"
        exclude = ['task_created_date','task_assign_By','task_status','close_task_descriptions','close_task_date']


class closetaskForm(forms.ModelForm):

    class Meta:
        model = task
        fields = '__all__'
        exclude=['task_name','task_details','task_assign_date','file','task_assign_By','task_choice','close_task_date']

class AttendenceForm(forms.ModelForm):
    date_with_intime = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                                 attrs={'class': 'form-control datepicker',
                                                                        'min': min_date,
                                                                         'value': today, 'type': 'date'}),
                                      )
    date_with_outtime = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                               attrs={'class': 'form-control datepicker',
                                                                      'min': min_date,
                                                                       'value': today, 'type': 'date'}),
                                    )
    class Meta:
        model = attendence
        fields = '__all__'
        exclude = ['emp_name']


