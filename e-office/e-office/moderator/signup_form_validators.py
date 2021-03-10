from .models import CustomUser, notifications
from django import forms

def userExist(value):
    user_exist = CustomUser.objects.filter(username=value)
    if user_exist:
        raise forms.ValidationError('This username is taken, try different username')

def password(value):
    if len(value) < 8:
        raise forms.ValidationError('Password must have minimum 8 characters')

def emailExist(value):
    email_exist = CustomUser.objects.filter(email=value)
    if email_exist:
        raise forms.ValidationError('This email is already present, try different email')

