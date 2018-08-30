from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Yahoo(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.search_field = lambda: self.driver.find_element(By.ID, 'uh-search-box')

    def fill_search_field(self, text):
        self.browser_helper.wait_for_element(self.search_field)
        self.browser_helper.send_text_to_element(self.search_field, text)

