from django.test import SimpleTestCase
from django.urls import reverse

class MainTests(SimpleTestCase):
    def test_main_page_status(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_main_page_template(self):
        url =reverse('main')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'main.html')

class AboutTests(SimpleTestCase):
    def test_about_page(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
