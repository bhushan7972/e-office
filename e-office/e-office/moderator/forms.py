from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile, notifications, store, messages, store_msg
from .signup_form_validators import *
from .choices import *



class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(validators=[userExist,])
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(validators=[emailExist,])
    password1 = forms.CharField(widget=forms.PasswordInput,validators=[password,],label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput,validators=[password,],label='Confirm password')

    email.widget.attrs.update({'placeholder':'Enter a valid Email Here'})
    username.widget.attrs.update({'placeholder':'Enter a username Here'})
    first_name.widget.attrs.update({'placeholder':'First Name'})
    last_name.widget.attrs.update({'placeholder':'Last Name'})

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','username', 'email')
        exclude = ['is_moderator', 'is_manager', 'is_hr', 'is_employee']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class profile(forms.ModelForm):

    maritial_status = forms.ChoiceField(choices=maritial_status,widget=forms.RadioSelect,required=True)
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect,required=True)

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','is_active' ]


class form(forms.ModelForm):

    class Meta:
        model = notifications
        fields = ['title', 'message']

class storage(forms.ModelForm):

    class Meta:
        model = store
        fields = '__all__'         


class message_form(forms.ModelForm):

    class Meta:
        model = messages
        fields = ['message']

class msg_storage(forms.ModelForm):

    class Meta:
        model = store_msg
        fields = '__all__'             