class BasePage:
    def __init__(self, browser):
        self.browser_helper = browser.browser_helper
        self.driver = browser.driver
