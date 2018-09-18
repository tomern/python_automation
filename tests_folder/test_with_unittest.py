import unittest
from selenium import webdriver


class TestClass1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_one(self):
        driver = self.driver
        driver.get("https://www.yahoo.com")

    def test_two(self):
        driver = self.driver
        driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.quit()
