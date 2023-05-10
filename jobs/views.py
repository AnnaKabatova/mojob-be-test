from rest_framework import generics, status
from rest_framework.response import Response
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer, JobHeaderSerializer
from .utils import send_job_created_email, send_job_updated_email


class CreateJobWithHeaderView(generics.CreateAPIView):
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        header_data = self.request.data.get('header')
        header_serializer = JobHeaderSerializer(data=header_data)
        if header_serializer.is_valid():
            header_serializer.save(job=job)
        send_job_created_email(job.id)
        return Response(
            "Job with header created successfully",
            status=status.HTTP_201_CREATED
        )


class UpdateJobWithHeaderView(generics.UpdateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def perform_update(self, serializer):
        job = serializer.save()
        header_data = self.request.data.get('header')
        header_serializer = JobHeaderSerializer(job.header, data=header_data)
        if header_serializer.is_valid():
            header_serializer.save(job=job)
        send_job_updated_email(job.id, job.header.rich_title_text, header_serializer.data.get('rich_title_text'))
        return Response(
            "Job with header updated successfully",
            status=status.HTTP_200_OK
        )


class DeleteJobWithHeaderView(generics.DestroyAPIView):
    queryset = Job.objects.all()

    def perform_destroy(self, instance):
        send_job_updated_email(instance.id, instance.header.rich_title_text, "Job Deleted")
        instance.delete()
        return Response(
            "Job with header deleted successfully",
            status=status.HTTP_204_NO_CONTENT
        )


class GetJobWithSerializedHeaderView(generics.RetrieveAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class GetUserApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Application.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
