from django.test import TestCase

class SmokeTest(TestCase):
    def test_incorrect_assumption(self):
        self.assertEqual("yes", "no")