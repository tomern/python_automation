from selenium import webdriver
from browser_folder.browser_helper import BrowserHelper


class Browser:
    def __init__(self):
        # self.driver = webdriver.Remote("http://localhost:4445/wd/hub", {"browserName": "chrome"})
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\tomern23\Desktop\chromedriver.exe")
        self.browser_helper = BrowserHelper(self.driver)
        self.driver.maximize_window()

    def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def get_url(self):
        return self.driver.current_url

    def maximize(self):
        self.driver.maximize_window()
