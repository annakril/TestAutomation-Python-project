import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from pages.search_product_page import SearchProductPage
from locators import SearchProductLocators
from test_data.data import DataProduct


class SearchProductInvalidTest(BaseTest):
    def setUp(self):
        super().setUp()
        ar = AcceptRodoPage(self.driver)
        ar.accept_rodo()

    def test_search_product_invalid(self):
        sp = SearchProductPage(self.driver)
        sp.search_product(DataProduct.invalid_product_name)
        sr = self.driver.find_element(*SearchProductLocators.SEARCHING_RESULT)
        actual_searching_result_text = sr.text

        self.assertEqual(DataProduct.expected_invalid_searching_result_text, actual_searching_result_text, f'Expected text to search for products that do not exist: {DataProduct.expected_invalid_searching_result_text}, differ from actual {actual_searching_result_text}')


if __name__ == "__main__":
    unittest.main(verbosity=2)
