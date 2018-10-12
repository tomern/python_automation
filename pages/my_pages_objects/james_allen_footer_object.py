from page_objects import PageObject, PageElement


class JamesAllenFooter(PageObject):
    newsletter_input = PageElement(id_='newsletter-input')
    male_btn = PageElement(name='Male')

    def signup_email_list(self, user):
        self.w.wait_until(lambda f: self.newsletter_input, 30)
        self.newsletter_input = user['username']
        self.male_btn.click()
