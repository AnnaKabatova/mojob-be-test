from rest_framework import serializers
from .models import Job, JobHeader, Application
from django.utils.html import strip_tags


class JobHeaderSerializer(serializers.ModelSerializer):
    plain_title_text = serializers.SerializerMethodField()

    def get_plain_title_text(self, obj):
        return strip_tags(obj.rich_title_text)

    class Meta:
        model = JobHeader
        fields = [
            "rich_title_text",
            "rich_subtitle_text",
            "plain_title_text"
        ]


class JobSerializer(serializers.ModelSerializer):
    header = JobHeaderSerializer()

    class Meta:
        model = Job
        fields = ["id", "name", "type", "header"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["user", "job"]
