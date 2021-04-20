import HtmlTestRunner
import unittest
from tests.accept_rodo_test import AcceptRodoTest
from tests.add_to_basket_test import AddToBasket
from tests.base_test import BaseTest
from tests.change_quantity_product_test import ChangeQuantityProduct
from tests.check_id_searched_product_valid_ddt_test import CheckIdSearchedProductValid
from tests.delete_product_from_basket_test import DeleteBasket
from tests.go_to_basket_test import GoToBasket
from tests.search_product_invalid_test import SearchProductInvalidTest
import os

dir = os.getcwd()

accept_rodo_test = unittest.TestLoader().loadTestsFromTestCase(AcceptRodoTest)
add_to_basket_test = unittest.TestLoader().loadTestsFromTestCase(AddToBasket)
base_test = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
change_quantity_product_test = unittest.TestLoader().loadTestsFromTestCase(ChangeQuantityProduct)
check_id_searched_product_valid_ddt_test = unittest.TestLoader().loadTestsFromTestCase(CheckIdSearchedProductValid)
delete_product_from_basket_test = unittest.TestLoader().loadTestsFromTestCase(DeleteBasket)
go_to_basket_test = unittest.TestLoader().loadTestsFromTestCase(GoToBasket)
search_product_invalid_test = unittest.TestLoader().loadTestsFromTestCase(SearchProductInvalidTest)

test_suite = unittest.TestSuite([accept_rodo_test, add_to_basket_test, base_test, change_quantity_product_test, check_id_searched_product_valid_ddt_test, delete_product_from_basket_test, go_to_basket_test, search_product_invalid_test])


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_results'))
