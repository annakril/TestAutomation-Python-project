import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from pages.search_product_page import SearchProductPage
from pages.product_page import ProductPage
from locators import CompleteOrderLocators
from test_data.data import DataProduct
from test_data.data import DataBasket


class GoToBasket(BaseTest):
    def setUp(self):
        super().setUp()
        ar = AcceptRodoPage(self.driver)
        ar.accept_rodo()
        sp = SearchProductPage(self.driver)
        sp.search_product(DataProduct.valid_product_name)
        flp = SearchProductPage(self.driver)
        flp.first_element_list()
        ab = ProductPage(self.driver)
        ab.add_to_basket()

    def test_go_to_basket(self):
        rz = ProductPage(self.driver)
        rz.go_to_basket()
        actual_cart_title_basket_text = self.driver.find_element(*CompleteOrderLocators.BASKET_CART_TITLE).text

        self.assertEqual(DataBasket.expected_cart_title_basket_text, actual_cart_title_basket_text, f'Expected cart title after go to the basket: "{DataBasket.expected_cart_title_basket_text}", actual text is differ "{actual_cart_title_basket_text}"')


if __name__ == "__main__":
    unittest.main(verbosity=2)
