from django.test import TestCase

from jobs.serializers import JobHeaderSerializer


class JobHeaderSerializerTests(TestCase):
    def test_job_header_serializer(self):
        header_data = {
            "rich_title_text": "Rich Title",
            "rich_subtitle_text": "Rich Subtitle",
        }

        serializer = JobHeaderSerializer(data=header_data)
        self.assertTrue(serializer.is_valid())

        header_instance = serializer.save()

        self.assertEqual(
            header_instance.rich_title_text, header_data["rich_title_text"]
        )
        self.assertEqual(
            header_instance.rich_subtitle_text,
            header_data["rich_subtitle_text"]
        )
