import pytest
from configuration_folder import configuration as cfg
from pages.james_signup_thanks_popup import JamesSignupThanksPopup
from pages.james_allen_footer import JamesAllenFooter


@pytest.mark.flaky(reruns=cfg.rerun, reruns_delay=cfg.reruns_delay)
@pytest.mark.element
def test_three(browser, app_config):
    browser.navigate(app_config.urls['jamesallen_url'])
    james_allen_footer = JamesAllenFooter(browser)
    james_allen_footer.signup_email_list(app_config.user_jamesallen)
    james_signup_thanks_popup = JamesSignupThanksPopup(browser)
    james_signup_thanks_popup.close_register_popup()
    assert james_signup_thanks_popup.check_popup_disabled()
