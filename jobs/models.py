from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    class JobTypes(models.TextChoices):
        FULL_TIME = "full-time", "Full Time"
        PART_TIME = "part-time", "Part Time"

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=JobTypes.choices)


class JobHeader(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="header")
    rich_title_text = models.TextField()
    rich_subtitle_text = models.TextField()


class Application(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
