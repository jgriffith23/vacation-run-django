from selenium import webdriver
import unittest

class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Vacation Run", self.browser.title)
        self.fail("Finish writing this test!")

if __name__ == "__main__":
    unittest.main(warnings="ignore")