from page_objects import PageObject, PageElement


class JamesSignupThanksPopup(PageObject):
    close_thanx_rsgister = PageElement(id_='closeThanxRegister')
    popup_div = PageElement(xpath='//div[@id="absoluteDiv"][@class="Visible"]')

    def close_register_popup(self):
        self.close_thanx_rsgister.click()

    def check_popup_disabled(self):
        return self.w.wait_until_not(lambda f: self.popup_div, 30)
