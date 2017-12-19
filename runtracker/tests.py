from django.test import TestCase
from django.urls import resolve
from runtracker.views import HomePageView
from django.test import Client

class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_resolves_to_home(self):
         result = resolve("/")
         self.assertEqual(result.func.view_class, HomePageView)

    def test_homepage_has_correct_template(self):
        result = self.client.get("/")
        html = result.content
        self.assertTrue(html.startswith(b"<!DOCTYPE html>"))
        self.assertIn(b"<title>Vacation Run</title>", html)
        self.assertTrue(html.endswith(b"</html>"))

