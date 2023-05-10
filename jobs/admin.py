from django.contrib import admin
from .models import Job, JobHeader, Application


admin.site.register(Job)
admin.site.register(JobHeader)
admin.site.register(Application)
