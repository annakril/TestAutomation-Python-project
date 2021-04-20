from pages.base_page import BasePage
from locators import SearchProductLocators
from locators import SearchedProductLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SearchProductPage(BasePage):
    def search_product(self, product_name):
        si = self.driver.find_element(*SearchProductLocators.SEARCH_INPUT)
        si.send_keys(product_name)
        si.send_keys(Keys.ENTER)

    def first_element_list(self):
        flp = self.driver.find_element(*SearchedProductLocators.FIRST_PRODUCT_LIST)
        actions = ActionChains(self.driver)
        actions.move_to_element(flp)
        actions.click(flp).perform()
