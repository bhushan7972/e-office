from django import forms
from .models import *
from .models import Post
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



class postForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['author','post_date']

class manager_leave_form(forms.ModelForm):
    leave_from_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    leave_to_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = manger_leave
        fields = '__all__'
        exclude= ['manager_name']

