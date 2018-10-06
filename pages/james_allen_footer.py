from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JamesAllenFooter(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.newsletter_input = lambda: self.driver.find_element(By.ID, 'newsletter-input')
        self.male_btn = lambda: self.driver.find_element(By.NAME, 'Male')

        self.browser_helper.wait_for_url('james')

    def signup_email_list(self, user):
        self.browser_helper.wait_for_element(self.newsletter_input)
        self.browser_helper.send_text_to_element(self.newsletter_input, user['username'])
        self.browser_helper.wait_for_element(self.male_btn)
        self.browser_helper.click_element(self.male_btn)
