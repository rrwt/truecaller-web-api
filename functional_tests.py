import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:8000"
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_phone_number_and_get_result(self):
        self.browser.get(self.url)

        self.assertIn("Truecaller", self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Truecaller User Profiler", header_text)

        inputbox = self.browser.find_element_by_id("phone-number")
        time.sleep(1)
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a phone number for verification",
        )
        inputbox.send_keys("5215544975736")
        time.sleep(2)
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id("user-detail-table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "Name" for row in rows))

        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
