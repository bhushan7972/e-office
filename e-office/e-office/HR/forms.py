from django import forms
from .models import hrP
from moderator.choices import *



class hr_profile(forms.ModelForm):

    maritial_status = forms.ChoiceField(choices=maritial_status,widget=forms.RadioSelect,required=True)
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect,required=True)
    

    class Meta:
        model = hrP
        fields = '__all__'
        exclude = ['user','is_active' ]