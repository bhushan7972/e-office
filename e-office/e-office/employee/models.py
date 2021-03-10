from django.db import models
from moderator.choices import *
from moderator.validators import validate_file_size, empty_file
from moderator.models import CustomUser

# Create your models here.
class employeeP(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default = False)
    department = models.CharField(max_length=20, choices=department, blank=False,null=False)
    designation = models.CharField(max_length=100)
    maritial_status = models.CharField(max_length=20, choices=maritial_status)
    gender = models.CharField(max_length=20, choices=gender)
    short_bio = models.TextField(max_length=150, blank=False,null=False)
    city = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=50,choices=states,blank=False,null=False)
    profile_picture = models.ImageField(upload_to='employee/profile/avatar/%Y/%m/%d', null=False, blank=False, validators=[validate_file_size, empty_file])
    
    def __str__(self):
        s = str(self.user)
        return (s)

class employee_leave(models.Model):

    leave_from_date = models.DateTimeField(null=True)
    leave_to_date = models.DateTimeField(null=True)
    leave_reason = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    employee_name = models.ForeignKey(employeeP, on_delete=models.CASCADE)        