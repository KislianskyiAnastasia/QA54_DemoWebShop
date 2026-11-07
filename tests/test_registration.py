from pages.registration_page import RegistrationPage

FIRST_NAME = "Anastasia"
LAST_NAME = "Kisliy"
VALID_EMAIL = "Kislianskyi@gmail.com"
VALID_PASSWORD = "Zxczxc26!"
CONFIRM_PASSWORD = "Zxczxc26!"

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.gender_female()
    registration_page.fill_first_name_field(FIRST_NAME)
    registration_page.fill_last_name_field(LAST_NAME)
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.confirm_password(CONFIRM_PASSWORD)
    registration_page.click_registration_button()

    assert registration_page.is_registration_completed()
