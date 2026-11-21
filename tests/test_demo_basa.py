import pytest

from pages.demo_shop_page import ShopPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from tests.data import VALID_EMAIL, VALID_PASSWORD


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.shop_page = ShopPage(driver)

    @pytest.fixture
    def login_form_opened(self, setup):
        self.login_page.open_login_page()

    @pytest.fixture
    def logged_in(self, login_form_opened):
        self.login_page.login(VALID_EMAIL, VALID_PASSWORD)
        assert self.login_page.is_log_out_displayed(), "Precondition failed: login"