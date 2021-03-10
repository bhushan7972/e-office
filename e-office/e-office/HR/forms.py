from django import forms
from .models import hrP,Opening
from moderator.choices import *
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from datetime import datetime, time, date, timedelta
min_date = date.today()
max_date = date.today() + timedelta(1*31)


class hr_profile(forms.ModelForm):

    maritial_status = forms.ChoiceField(choices=maritial_status,widget=forms.RadioSelect,required=True)
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect,required=True)
    

    class Meta:
        model = hrP
        fields = '__all__'
        exclude = ['user','is_active' ]

class openingform(forms.ModelForm):
    starting_date_to_apply = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                                    attrs={'class': 'form-control datepicker',
                                                                           'min': min_date,
                                                                           'max': max_date, 'value': max_date,
                                                                           'type': 'date'}),
                                         )

    last_date_to_apply = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': max_date, 'value': max_date, 'type': 'date'}),
                                  )
    class Meta:
        model = Opening
        fields = '__all__'
        exclude = ['hruser','postdate']



