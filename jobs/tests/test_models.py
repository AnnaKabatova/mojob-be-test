from django.contrib.auth.models import User
from django.test import TestCase

from jobs.models import Application, Job, JobHeader


class JobModelTest(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            name="Job name",
            type=Job.JobTypes.FULL_TIME
        )

    def test_name_label(self):
        field_label = self.job._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_type_label(self):
        field_label = self.job._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_name_max_length(self):
        max_length = self.job._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_name(self):
        expected_object_name = self.job.name
        self.assertEqual(expected_object_name, str(self.job))


class JobHeaderModelTest(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            name="Job name",
            type=Job.JobTypes.FULL_TIME
        )
        self.job_header = JobHeader.objects.create(
            job=self.job,
            rich_title_text="Rich title text",
            rich_subtitle_text="Rich subtitle text"
        )

    def test_rich_title_text_label(self):
        field_label = self.job_header._meta.get_field("rich_title_text").verbose_name
        self.assertEqual(field_label, "rich title text")

    def test_rich_subtitle_text_label(self):
        field_label = self.job_header._meta.get_field("rich_subtitle_text").verbose_name
        self.assertEqual(field_label, "rich subtitle text")

    def test_object_name_is_rich_title_text(self):
        expected_object_name = self.job_header.rich_title_text
        self.assertEqual(expected_object_name, str(self.job_header))


class ApplicationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.job = Job.objects.create(
            name="Job name",
            type=Job.JobTypes.FULL_TIME
        )
        self.application = Application.objects.create(
            user=self.user,
            job=self.job
        )

    def test_user_label(self):
        field_label = self.application._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_job_label(self):
        field_label = self.application._meta.get_field("job").verbose_name
        self.assertEqual(field_label, "job")

    def test_object_name_is_user_job(self):
        expected_object_name = f"{self.user} - {self.job}"
        self.assertEqual(expected_object_name, str(self.application))
