from selenium import webdriver
from browser_folder.browser_helper import BrowserHelper


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.browser_helper = BrowserHelper(self.driver)

    def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def get_url(self):
        return self.driver.current_url

    def maximize(self):
        self.driver.maximize_window()
