from django.contrib import admin
from .models import managerP
from .models import Post
from .models import postcomment
from .models import manger_leave,task,attendence

# Register your models here.
admin.site.register(managerP)
admin.site.register(Post)

admin.site.register(manger_leave)
admin.site.register(postcomment)
admin.site.register(task)
admin.site.register(attendence)