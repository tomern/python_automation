from page_objects import PageObject, PageElement


class GooglePage(PageObject):
        search_field = PageElement(name='q')
        gmail_btn = PageElement(xpath='//*[contains(text(),"Gmail")]')
