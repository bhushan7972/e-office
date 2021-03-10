from django import forms
from .models import employeeP,employee_leave
from moderator.choices import maritial_status,gender
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
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    leave_to_date = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = employee_leave
        fields = '__all__'   
        exclude= ['employee_name']     