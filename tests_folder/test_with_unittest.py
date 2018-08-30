import unittest
from selenium import webdriver
import pytest


class TestClass1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:4445/wd/hub", {"browserName": "chrome"})
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



@pytest.fixture()
def this_is:
    a = 4
    return a

def test_one:
    a = 1
    assert a > 0

def test_two:
    a = 2
    print(a)
    assert a > 0
