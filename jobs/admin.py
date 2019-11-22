from django.contrib import admin
from .models import Job, JobFileUpload, JobComment

# Register your models here.
admin.site.register(Job)
admin.site.register(JobFileUpload)
admin.site.register(JobComment)