from page_objects import PageObject, PageElement


class JamesAllenFooter(PageObject):
    newsletter_input = PageElement(id_='newsletter-input')
    male_btn = PageElement(name='Male')

    def signup_email_list(self, user):
        # self.newsletter_input = user['username']
        self.newsletter_input.click()
        a = 4
