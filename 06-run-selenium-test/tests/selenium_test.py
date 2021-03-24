import unittest
import pytest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os 

DRIVE_HOST = format('http://' + os.environ.get('DRIVER_HOST') + ':4444/wd/hub')

print(DRIVE_HOST)

class PythonOrgSearch(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term = "WD My Passport 4TB"

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=DRIVE_HOST,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_load_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Amazon", driver.title)

    def test_search_for_a_term(self):
        self.driver.get(self.base_url)
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term, self.driver.title)
        self.assertNotIn("No results found.", self.driver.page_source)
    
    def test_simple_search(self):
        self.driver.get("https://example.testproject.io/web/")
        self.driver.find_element_by_css_selector("#name").send_keys("John Smith")
        self.driver.find_element_by_css_selector("#password").send_keys("12345")
        self.driver.find_element_by_css_selector("#login").click()
        passed = self.driver.find_element_by_css_selector("#logout").is_displayed()

        print("Test passed") if passed else print("Test failed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports/"))
