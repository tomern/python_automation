from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Google(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.search_field = lambda: self.driver.find_element(By.NAME, 'q')
        self.gmail_btn = lambda: self.driver.find_element(By.XPATH, '//a[@dir="ltr"][1]')

    def click_on_gmail_btn(self):
        self.browser_helper.wait_for_element(self.gmail_btn)
        self.browser_helper.click_element(self.gmail_btn)

    def fill_search_field(self, text):
        self.browser_helper.wait_for_element(self.search_field)
        self.browser_helper.send_text_to_element(self.search_field, text)

