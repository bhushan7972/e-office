from django.db import models
from moderator.choices import *
from moderator.validators import validate_file_size, empty_file
from moderator.models import CustomUser
from HR.models import Opening

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
    leave_from_date = models.DateTimeField(auto_now_add=True,null=True)
    leave_to_date = models.DateTimeField(auto_now_add=True,null=True)
    leave_reason = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    employee_name = models.ForeignKey(employeeP, on_delete=models.CASCADE)
    work_choice = [('accepted', 'accepted'), ('rejected', 'rejected')]
    work_status = models.CharField(max_length=20, choices=work_choice, default='empty')

    @property
    def total_leave_day(self):
        return (self.leave_to_date - self.leave_from_date).days+1


class job_apply(models.Model):
    job_title = models.ForeignKey(Opening,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobileno = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gender,null=True)
    Qualification = models.CharField(max_length=20)
    birthdate = models.DateTimeField(auto_now_add=True )
    yearofpassing = models.IntegerField()
    yearofexperience = models.FloatField(default=0.0)
    resume = models.FileField()

    def __str__(self):
        return str(self.firstname)