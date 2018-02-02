import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False


class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_homepage(self):
        # A user can visit the homepage
        self.browser.get("http://localhost:8000")

        # A user should see a title and homepage that talk about
        # running for your vacation
        self.assertIn("Vacation Workouts", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Vacation Workouts", header_text)


# if __name__ == "__main__":
#     unittest.main(warnings="ignore")