from pages.login_page import GooglePage
from time import sleep


def test_test_page_objects(selenium):
    google_page = GooglePage(selenium, root_uri='https://www.google.com/')
    google_page.get('')
    sleep(5)
    google_page.gmail_btn.click()
