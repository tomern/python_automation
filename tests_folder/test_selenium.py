import pytest
from pages.google_page import Google
from configuration_folder import configuration as cfg
from pages.james_signup_thanks_popup import JamesSignupThanksPopup
from pages.james_allen_footer import JamesAllenFooter


# @pytest.mark.flaky(reruns=cfg.rerun, reruns_delay=1)
# @pytest.mark.element
# def test_one(browser):
#     browser.navigate("https://www.google.com")
#     google = Google(browser)
#     google.click_on_gmail_btn()
#     assert 'gmail' in browser.get_url()
#
#
# @pytest.mark.element
# def test_two(browser):
#     browser.navigate("https://www.google.com")
#     google = Google(browser)
#     search_term = 'test'
#     google.fill_search_field(search_term+'\n')
#     assert search_term in browser.get_url()


@pytest.mark.element
def test_three(browser, app_config):
    browser.navigate(app_config.jamesallen_url)
    james_allen_footer = JamesAllenFooter(browser)
    james_allen_footer.signup_email_list(app_config.user_jamesallen)
    james_signup_thanks_popup = JamesSignupThanksPopup(browser)
    james_signup_thanks_popup.close_register_popup()
    assert james_signup_thanks_popup.check_popup_disabled()
