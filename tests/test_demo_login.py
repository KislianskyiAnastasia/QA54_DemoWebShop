from tests.data import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, UNREGISTERED_EMAIL, WRONG_PASSWORD
from tests.test_demo_basa import BaseTest


class TestLogin(BaseTest):

    def test_login_form_is_available(self):
        assert self.login_page.is_login_icon_displayed(), "Login icon not found"
        self.login_page.open_login_page()
        assert self.login_page.are_login_form_elements_displayed(), \
            "Login form elements are not displayed"

    def test_valid_login_success(self, login_form_opened):
        self.login_page.login(VALID_EMAIL, VALID_PASSWORD)
        assert self.login_page.is_log_out_displayed(), "Log out button is not displayed"

    def test_with_invalid_email(self, login_form_opened):
        self.login_page.login(INVALID_EMAIL,VALID_PASSWORD)
        assert self.login_page.is_invalid_email_message(), \
            "Invalid Email format message is not displayed"

    def test_with_unregistered_email(self, login_form_opened):
        self.login_page.login(UNREGISTERED_EMAIL, VALID_PASSWORD)
        assert self.login_page.is_wrong_email_message(), \
            "Account not found message is not displayed"

    def test_with_wrong_password(self, login_form_opened):
        self.login_page.login(VALID_EMAIL, WRONG_PASSWORD)
        assert self.login_page.is_wrong_password_message(), \
            "Incorrect credentials message is not displayed"