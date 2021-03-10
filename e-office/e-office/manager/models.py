from django.db import models
from moderator.choices import *
from moderator.validators import validate_file_size, empty_file
from moderator.models import CustomUser
from employee.models import employeeP,employee_leave

# Create your models here.
class managerP(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default = False)
    department = models.CharField(max_length=20, choices=department, blank=False,null=False)
    designation = models.CharField(max_length=100)
    maritial_status = models.CharField(max_length=20, choices=maritial_status)
    gender = models.CharField(max_length=20, choices=gender)
    short_bio = models.TextField(max_length=150, blank=False,null=False)
    city = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=50,choices=states,blank=False,null=False)
    profile_picture = models.ImageField(upload_to='manager/profile/avatar/%Y/%m/%d', null=False, blank=False, validators=[validate_file_size, empty_file])

    def __str__(self):
        s = str(self.user)
        return (s)



class Post(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now=True)
    content=models.TextField(max_length=500)
    author = models.ForeignKey(managerP, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class postcomment(models.Model):
    comment = models.TextField(max_length=200)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.sender)

class manger_leave(models.Model):

    leave_from_date = models.DateTimeField(null=True)
    leave_to_date = models.DateTimeField(null=True)
    leave_reason = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    manager_name = models.ForeignKey(managerP, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.manager_name)

class task(models.Model):
    task_name = models.CharField(max_length=200)
    task_details = models.TextField(max_length=500)
    task_created_date = models.DateTimeField(auto_now_add=True,null=True)
    task_assign_date = models.DateTimeField(null=True)
    file=models.FileField(null=True)
    task_assign_By = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default="")
    task_choice=[('Completed','Completed'),('Working','Working'),('Waiting Aprove','Waiting Aprove'),('Incomplete close','Incomplete close')]
    task_status = models.CharField(max_length=20,choices=task_choice,default='Waiting Aprove')
    close_task_descriptions= models.TextField(max_length=1000,null=True)
    close_task_date= models.DateTimeField(null=True)


class attendence(models.Model):

    emp_name =models.ForeignKey(employeeP,on_delete=models.CASCADE,default="")
    date_with_intime = models.DateTimeField(null=True)
    date_with_outtime = models.DateTimeField(null=True)
    work_choice = [('Working', 'Working'), ('Waiting Aprove', 'Waiting Aprove'), ('wontedleave', 'wontedleave'),
                   ('onleave', 'onleave')]
    work_status = models.CharField(max_length=20, choices=work_choice, default='working')
    month_choice=[('January','January'),('February','February'),('March','March'),('April','April'),(' May',' May'),('June','June'),('July','July'),('August','August'),('September','September'),('October','October'),('November','November'),('December','December')]
    select_month = models.CharField(max_length=20,choices=month_choice,default="")

    def __str__(self):
        return str(self.emp_name)
