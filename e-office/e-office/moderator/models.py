from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import *
from .validators import validate_file_size, empty_file

class CustomUser(AbstractUser):
    
    is_moderator = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Profile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default = False)
    department = models.CharField(max_length=20, choices=department, blank=False,null=False)
    designation = models.CharField(max_length=100)
    maritial_status = models.CharField(max_length=20, choices=maritial_status)
    gender = models.CharField(max_length=20, choices=gender)
    short_bio = models.TextField(max_length=150, blank=False,null=False)
    city = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=50,choices=states,blank=False,null=False)
    profile_picture = models.ImageField(upload_to='moderator/profile/avatar/%Y/%m/%d', null=False, blank=False, validators=[validate_file_size, empty_file])
    
    def __str__(self):
        s = str(self.user)
        return (s)

class notifications(models.Model):

    
    sender = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class store(models.Model):

    sn = models.IntegerField()
    notification_id = models.IntegerField()


class messages(models.Model):

    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sender')    
    receivar = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='receiver')    
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class store_msg(models.Model):

    sn = models.IntegerField()
    msg_id = models.IntegerField()    
       