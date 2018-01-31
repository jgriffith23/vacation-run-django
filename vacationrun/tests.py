# from selenium import webdriver
# import unittest

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False


class NewUserTest(StaticLiveServerTestCase):

    # def setUp(self):
    #     self.browser = webdriver.Firefox()
    #
    # def tearDown(self):
    #     self.browser.quit()

    @classmethod
    def setUpClass(cls):
        super(NewUserTest, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(NewUserTest, cls).tearDownClass()

    def test_can_visit_homepage(self):
        # A user can visit the homepage
        self.selenium.get("http://localhost:8000")

        # A user should see a title and homepage that talk about
        # running for your vacation
        self.assertIn("Vacation Run", self.selenium.title)
        header_text = self.selenium.find_element_by_tag_name("h1").text
        self.assertIn("Let's Run for a Vacation!", header_text)

    # def test_can_calculate_runs_for_vacation_from_homepage(self):
    #     # A user should be able to enter how far they run in
    #     # a week and a destination to see how many weeks they'd have
    #     # to run to go on vacation there.
    #     miles_box = self.selenium.find_element_by_id("miles")
    #     dest_city_box = self.selenium.find_element_by_id("dest-city")
    #     dest_country_box = self.selenium.find_element_by_id("dest-country")
    #     origin_city_box = self.selenium.find_element_by_id("origin-city")
    #     origin_country_box = self.selenium.find_element_by_id("origin-country")
    #
    #     miles_box.send_keys("15")
    #     dest_city_box.send_keys("Tokyo")
    #     dest_country_box.send_keys("Japan")
    #     origin_city_box.send_keys("San Francisco")
    #     origin_country_box.send_keys("USA")
    #
    #
    #     calculate_button = self.browser.find_element_by_id("calculate")
    #     calculate_button.click()
    #     time.sleep(1)
    #
    #     # Tokyo is 5151 miles away from SF.
    #     weeks = self.browser.find_element_by_id("weeks")
    #     self.assertTrue(weeks.text, "344")
    #
    #     self.fail("Finish writing the code for this test!")

# if __name__ == "__main__":
#     unittest.main(warnings="ignore")