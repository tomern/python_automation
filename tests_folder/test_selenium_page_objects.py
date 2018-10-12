from pages.my_pages_objects.james_allen_footer_object import JamesAllenFooter
# from pages.my_pages_objects.james_signup_thanks_popup_object import JamesSignupThanksPopup


def test_test_page_objects(selenium, app_config):
    selenium.get(app_config.urls['jamesallen_url'])
    james_allen_footer = JamesAllenFooter(selenium)
    james_allen_footer.newsletter_input = 'asdfasdf'
    # james_allen_footer.signup_email_list(app_config.user_jamesallen)
    # james_signup_thanks_popup = JamesSignupThanksPopup(selenium)
    # james_signup_thanks_popup.close_register_popup()
    # assert james_signup_thanks_popup.check_popup_disabled()
