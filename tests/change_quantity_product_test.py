import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from pages.search_product_page import SearchProductPage
from pages.product_page import ProductPage
from locators import ChangeProductQuantityLocators
from test_data.data import DataProduct


class ChangeQuantityProduct(BaseTest):
    def setUp(self):
        super().setUp()
        ar = AcceptRodoPage(self.driver)
        ar.accept_rodo()
        sp = SearchProductPage(self.driver)
        sp.search_product(DataProduct.valid_product_name)
        flp = SearchProductPage(self.driver)
        flp.first_element_list()

    def test_change_quantity_plus(self):
        qp = ProductPage(self.driver)
        qp.change_quantity_plus()

        actual_quantity_value = self.driver.find_element(*ChangeProductQuantityLocators.QUANTITY_VALUE).get_attribute('value')

        self.assertEqual(DataProduct.expected_quantity_value, actual_quantity_value, f'Expected quantity value is: "{DataProduct.expected_quantity_value}", but actual is differ: "{actual_quantity_value}"')


if __name__ == "__main__":
    unittest.main(verbosity=2)
