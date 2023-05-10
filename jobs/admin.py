from django.contrib import admin

from .models import Application, Job, JobHeader

admin.site.register(Job)
admin.site.register(JobHeader)
admin.site.register(Application)
