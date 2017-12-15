from django.test import TestCase
from django.urls import resolve
from runtracker.views import HomePageView

class HomePageTest(TestCase):
    def test_root_resolves_to_home(self):
         found = resolve('/')
         self.assertEqual(found.view_name, "home")
