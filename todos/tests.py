from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

# Create your tests here.


class ImageUploadTests(TestCase):
    def test_get_displays_upload_form(self):
        response = self.client.get(reverse("get_info"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'enctype="multipart/form-data"')
        self.assertContains(response, 'type="file"')

    def test_post_accepts_an_uploaded_image(self):
        image = SimpleUploadedFile(
            "test.png",
            b"\x89PNG\r\n\x1a\n",
            content_type="image/png",
        )

        response = self.client.post(reverse("get_info"), {"image": image})

        self.assertEqual(response.status_code, 200)
