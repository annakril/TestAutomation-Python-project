import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from pages.search_product_page import SearchProductPage
from pages.product_page import ProductPage
from locators import AddToBasketLocators
from test_data.data import DataProduct
from test_data.data import DataBasket


class AddToBasket(BaseTest):
    def setUp(self):
        super().setUp()
        ar = AcceptRodoPage(self.driver)
        ar.accept_rodo()
        sp = SearchProductPage(self.driver)
        sp.search_product(DataProduct.valid_product_name)
        flp = SearchProductPage(self.driver)
        flp.first_element_list()

    def test_add_to_basket(self):
        ab = ProductPage(self.driver)
        ab.add_to_basket()

        actual_added_to_basket_confirmation_pop_up_text = self.driver.find_element(*AddToBasketLocators.ADDED_TO_BASKET_CONFIRMATION_POPUP).text

        self.assertEqual(DataBasket.expected_added_to_basket_confirmation_pop_up_text, actual_added_to_basket_confirmation_pop_up_text, f'Expected text after product added to basket: "{DataBasket.expected_added_to_basket_confirmation_pop_up_text}", actual text is differ "{actual_added_to_basket_confirmation_pop_up_text}"')


if __name__ == "__main__":
    unittest.main(verbosity=2)
