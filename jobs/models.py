from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    TYPES_CHOICES = (
        ("full-time", "Full Time"),
        ("part-time", "Part Time")
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPES_CHOICES)


class JobHeader(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="header")
    rich_title_text = models.TextField()
    rich_subtitle_text = models.TextField()


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
