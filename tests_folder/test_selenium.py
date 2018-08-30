import pytest
from browser_folder.browser import Browser
from pages.google_page import Google


rerun = 1

@pytest.fixture()
def browser():
    _browser = Browser()
    yield _browser
    _browser.quit()


@pytest.mark.flaky(reruns=rerun, reruns_delay=2)
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
    search_term = 'test'
    google.fill_search_field(search_term+'\n')
    assert search_term in browser.get_url()


