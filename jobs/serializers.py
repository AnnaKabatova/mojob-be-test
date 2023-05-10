from django.utils.html import strip_tags
from rest_framework import serializers

from .models import Application, Job, JobHeader


class JobHeaderSerializer(serializers.ModelSerializer):
    plain_title_text = serializers.SerializerMethodField(read_only=True)

    def get_plain_title_text(self, obj):
        return strip_tags(obj.rich_title_text)

    class Meta:
        model = JobHeader
        fields = ["rich_title_text", "rich_subtitle_text", "plain_title_text"]


class JobSerializer(serializers.ModelSerializer):
    header = JobHeaderSerializer()

    class Meta:
        model = Job
        fields = ["id", "name", "type", "header"]

    def create(self, validated_data):
        job_header_data = validated_data.pop("header", None)
        job = Job.objects.create(**validated_data)
        if job_header_data:
            JobHeader.objects.create(job=job, **job_header_data)
        return job

    def update(self, instance, validated_data):
        job_header_data = validated_data.pop("header", {})
        job_header_serializer = self.fields["header"]
        job_header_serializer.update(instance.header, job_header_data)
        return super().update(instance, validated_data)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["user", "job"]
