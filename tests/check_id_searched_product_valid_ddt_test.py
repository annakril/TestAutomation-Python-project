import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from pages.search_product_page import SearchProductPage
from locators import SearchedProductLocators
from test_utils import utils
from ddt import ddt, data, unpack
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(THIS_DIR, '..', 'test_data/product_list.csv')


@ddt
class CheckIdSearchedProductValid(BaseTest):
    def setUp(self):
        super().setUp()
        ar = AcceptRodoPage(self.driver)
        ar.accept_rodo()

    @data(*utils.get_data(file_path))
    @unpack
    def test_check_id_searched_product_valid(self, product_name, product_id):
        sp = SearchProductPage(self.driver)
        sp.search_product(product_name)

        flp = SearchProductPage(self.driver)
        flp.first_element_list()

        actual_product_id = self.driver.find_element(*SearchedProductLocators.PRODUCT_SEARCHED_LANDING_PAGE_ID).get_attribute('value')

        self.assertEqual(product_id, actual_product_id, f'Expected searched ID product is: "{product_id}", actual ID is differ "{actual_product_id}"')


if __name__ == "__main__":
    unittest.main(verbosity=2)
