from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Google(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.big_btn = lambda: self.driver.find_element(By.ID, 'lst-ib')

    def click_on_big_button(self):
        self.browser_helper.wait_for_element(self.big_btn)
        self.big_btn().click()

    def fill_search_field(self, text):
        self.browser.browserHelp.set_text(self.search_field, text)
        self.browser_helper.wait_for_element(self.big_btn)