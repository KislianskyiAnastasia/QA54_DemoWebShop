from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[href='/register']")
    GENDER = (By.ID, "gender-female")
    NAME_INPUT = (By.CSS_SELECTOR, "[name='FirstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[name='LastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='Password']")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "[name='ConfirmPassword']")
    BUTTON_REGISTRATION = (By.XPATH,"//input[@id='register-button']")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()

    def gender_female(self):
        self.driver.find_element(*self.GENDER).click()

    def fill_first_name_field(self,first_name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(first_name)

    def fill_last_name_field(self,last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_email_field(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)


    def fill_password_field(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def confirm_password(self,password):
        self.driver.find_element(*self.PASSWORD_CONFIRM).clear()
        self.driver.find_element(*self.PASSWORD_CONFIRM).send_keys(password)


    def click_registration_button(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION).click()

    def is_registration_completed(self):
        try:
            WebDriverWait(self.driver, timeout=10).until(
                expected_conditions.visibility_of_element_located(
                    (By.CLASS_NAME, "result")
                )
            )
            return True
        except TimeoutException:
            return False





