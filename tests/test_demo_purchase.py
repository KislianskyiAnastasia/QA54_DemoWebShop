from faker import Faker

from tests.test_demo_basa import BaseTest

fake = Faker()


def generate_address():
    return {
        "country": "Israel",
        "city": fake.city(),
        "address": fake.street_address(),
        "zip": fake.numerify("#######"),
        "phone": fake.numerify("05########"),
    }


class TestPurchase(BaseTest):

    def test_buy_one_product(self, logged_in):
        self.shop_page.open_category("Books")
        self.shop_page.open_product("Health Book")
        self.shop_page.add_to_cart()
        assert self.shop_page.is_product_added(), "Product was not added to the cart"

        self.shop_page.open_cart()
        self.shop_page.start_checkout()
        self.shop_page.complete_checkout(generate_address())

        assert "successfully processed" in self.shop_page.get_order_success_text(), \
            "Order was not placed"