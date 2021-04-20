import unittest
from tests.base_test import BaseTest
from pages.rodo_page import AcceptRodoPage
from locators import RodoLocators
from test_data.data import DataRodo


class AcceptRodoTest(BaseTest):
    def setUp(self):
        super().setUp()

    def test_accept_rodo(self):
        ar = AcceptRodoPage(self.driver)
        ar.accept_rodo()

        rodo_pop_up_state_displayed = self.driver.find_element(*RodoLocators.RODO_POPUP).get_attribute("style")

        self.assertEqual(DataRodo.expected_rodo_pop_up_state_displayed, rodo_pop_up_state_displayed, f'Rodo pop-up should have status: "{DataRodo.expected_rodo_pop_up_state_displayed}", but actual status is "{rodo_pop_up_state_displayed}"')


if __name__ == "__main__":
    unittest.main(verbosity=2)
