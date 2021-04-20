import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from pages.search_product_page import SearchProductPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from locators import DeleteProductLocators
from test_data.data import DataProduct
from test_data.data import DataBasket


class DeleteBasket(BaseTest):
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
        rz = ProductPage(self.driver)
        rz.go_to_basket()

    def test_delete_product_from_basket(self):
        dp = BasketPage(self.driver)
        dp.delete_product_from_basket()

        actual_empty_basket_info_text = self.driver.find_element(*DeleteProductLocators.EMPTY_BASKET_INFO).text

        self.assertIn(DataBasket.expected_empty_basket_info_text, actual_empty_basket_info_text, f'Expected information if the basket is empty, contains: "{DataBasket.expected_empty_basket_info_text}" actual text is differ "{actual_empty_basket_info_text}"')


if __name__ == "__main__":
    unittest.main(verbosity=2)
