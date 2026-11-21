from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

from pages.demo_basa_page import BasePage


class ShopPage(BasePage):
    CATEGORY_LINK = "(//ul[@class='top-menu']//a[normalize-space()='{}'])[1]"
    PRODUCT_LINK = "//h2[@class='product-title']/a[normalize-space()='{}']"
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input.add-to-cart-button")
    NOTIFICATION_BAR = (By.ID, "bar-notification")
    CART_ICON = (By.CSS_SELECTOR, "a.ico-cart")
    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    BILLING_COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    BILLING_CITY = (By.ID, "BillingNewAddress_City")
    BILLING_ADDRESS = (By.ID, "BillingNewAddress_Address1")
    BILLING_ZIP = (By.ID, "BillingNewAddress_ZipPostalCode")
    BILLING_PHONE = (By.ID, "BillingNewAddress_PhoneNumber")

    STEP_BUTTON = "//div[@id='{}-buttons-container']//input[@type='button']"
    CHECKOUT_STEPS = ["billing", "shipping", "shipping-method", "payment-method",
                      "payment-info", "confirm-order"]
    ORDER_SUCCESS = (By.XPATH, "//div[@class='section order-completed']//strong")

    def open_category(self, name):
        self.click_element((By.XPATH, self.CATEGORY_LINK.format(name)))

    def open_product(self, name):
        self.click_element((By.XPATH, self.PRODUCT_LINK.format(name)))

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def is_product_added(self):
        return self.is_element_visible(self.NOTIFICATION_BAR)

    def open_cart(self):
        self.click_element(self.CART_ICON)

    def start_checkout(self):
        self.click_element(self.TERMS_CHECKBOX)
        self.click_element(self.CHECKOUT_BUTTON)

    def fill_billing_address_if_needed(self, address):
        # If the account already has a saved address, the form is not shown.
        if self.is_element_visible(self.BILLING_CITY, timeout=5):
            self.select_by_text(self.BILLING_COUNTRY, address["country"])
            self.input_text(self.BILLING_CITY, address["city"])
            self.input_text(self.BILLING_ADDRESS, address["address"])
            self.input_text(self.BILLING_ZIP, address["zip"])
            self.input_text(self.BILLING_PHONE, address["phone"])

    def continue_step(self, step, required=True):
        locator = (By.XPATH, self.STEP_BUTTON.format(step))
        if not required and not self.is_element_visible(locator, timeout=3):
            return  # шаг пропущен сайтом, идём дальше
        try:
            self.click_element(locator)
        except TimeoutException:
            self.driver.save_screenshot(f"fail_{step}.png")
            print(f"FAILED at step: {step}, url: {self.driver.current_url}")
            raise

    def complete_checkout(self, address):
        self.fill_billing_address_if_needed(address)
        for step in self.CHECKOUT_STEPS:
            self.continue_step(step, required=(step != "shipping"))

    def get_order_success_text(self):
        return self.get_text(self.ORDER_SUCCESS)