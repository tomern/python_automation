from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class BrowserHelper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, el):
        el().click()

    def send_text_to_element(self, el, text):
        el().send_keys(text)

    def wait_for_element(self, el, time_out=10):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(lambda d: el().is_displayed())

