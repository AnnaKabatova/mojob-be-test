from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Application, Job
from .serializers import (
    ApplicationSerializer,
    JobHeaderSerializer,
    JobSerializer
)
from .utils import send_job_created_email, send_job_updated_email


class JobWithHeaderViewSet(ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Job.objects.all()

    def perform_create(self, serializer):
        job = serializer.save()
        send_job_created_email(job.id)

    def perform_update(self, serializer):
        job = serializer.save()
        header_data = self.request.data.get("header")
        header_serializer = JobHeaderSerializer(job.header, data=header_data)

        header_serializer.is_valid(raise_exception=True)
        header_serializer.save(job=job)

        send_job_updated_email(
            job.id, job.header.rich_title_text, header_data.get("rich_title_text")
        )

        return Response(
            "Job with header updated successfully", status=status.HTTP_200_OK
        )


class GetUserApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Application.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
