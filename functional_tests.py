import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:8000"
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_phone_number_and_get_result(self):
        self.browser.get(self.url)
        self.assertIn("Truecaller", self.browser.title)
        self.fail("Test Finished")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
