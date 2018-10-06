from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JamesSignupThanksPopup(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        # region elements
        self.close_thanx_rsgister = lambda: self.driver.find_element(By.ID, 'closeThanxRegister')
        self.popup_div = lambda: self.driver.find_element( By.XPATH, '//div[@id="absoluteDiv"][@class="Visible"]')
        # endregion elements

    def close_register_popup(self):
        self.browser_helper.wait_for_element(self.close_thanx_rsgister)
        self.browser_helper.click_element(self.close_thanx_rsgister)

    def check_popup_disabled(self):
        return self.browser_helper.wait_for_element_disappear(self.popup_div)

