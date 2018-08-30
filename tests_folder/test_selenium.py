import pytest
from browser_folder.browser import Browser
from time import sleep
from pages.google_page import Google


@pytest.fixture()
def browser():
    _browser = Browser()
    yield _browser
    _browser.quit()


@pytest.mark.element
def test_one(browser):
    browser.navigate("https://www.google.com")
    google = Google(browser)
    google.click_on_gmail_btn()
    assert 'gmail' in browser.get_url()


@pytest.mark.element
def test_two(browser):
    browser.navigate("https://www.google.com")
    google = Google(browser)
    google.click_on_gmail_btn()
    assert 'gmail' in browser.get_url()


