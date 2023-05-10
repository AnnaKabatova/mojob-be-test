from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from jobs.models import Application, Job
from jobs.serializers import ApplicationSerializer


class JobWithHeaderViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = self.get_auth_token()

    def get_auth_token(self):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "testpassword"},
            format="json",
        )
        return response.data["access"]

    def test_create_job_with_header_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

        response = self.client.post(
            reverse("jobs-list"),
            {
                "name": "Test Job",
                "type": "full-time",
                "header": {
                    "rich_title_text": "Rich Title",
                    "rich_subtitle_text": "Rich Subtitle",
                },
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_job_with_header_unauthenticated(self):
        response = self.client.post(
            reverse("jobs-list"),
            {
                "name": "Test Job",
                "type": "full-time",
                "header": {
                    "rich_title_text": "Rich Title",
                    "rich_subtitle_text": "Rich Subtitle",
                },
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_job_with_header_authenticated(self):
        job = Job.objects.create(name="Test Job", type="full-time")
        header_data = {
            "rich_title_text": "Updated Rich Title",
            "rich_subtitle_text": "Updated Rich Subtitle",
        }
        url = reverse("jobs-detail", kwargs={"pk": job.pk})
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

        response = self.client.patch(
            url,
            {"header": header_data},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_job_with_header_unauthenticated(self):
        job = Job.objects.create(name="Test Job", type="full-time")
        header_data = {
            "rich_title_text": "Updated Rich Title",
            "rich_subtitle_text": "Updated Rich Subtitle",
        }
        url = reverse("jobs-detail", kwargs={"pk": job.pk})

        response = self.client.patch(
            url,
            {"header": header_data},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class GetUserApplicationsViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = self.get_auth_token()

    def get_auth_token(self):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "testpassword"},
            format="json",
        )
        return response.data["access"]

    def test_get_user_applications_authenticated(self):
        job = Job.objects.create(name="Test Job", type="full-time")
        application = Application.objects.create(user=self.user, job=job)

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        url = reverse(
            "get_user_applications",
            kwargs={"user_id": self.user.id}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ApplicationSerializer(application)
        self.assertEqual(response.data, [serializer.data])

    def test_get_user_applications_unauthenticated(self):
        job = Job.objects.create(name="Test Job", type="full-time")
        Application.objects.create(user=self.user, job=job)

        url = reverse(
            "get_user_applications",
            kwargs={"user_id": self.user.id}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
