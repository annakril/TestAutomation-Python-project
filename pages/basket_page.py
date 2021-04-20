from pages.base_page import BasePage
from locators import DeleteProductLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def delete_product_from_basket(self):
        dp = self.driver.find_element(*DeleteProductLocators.DELETE_PRODUCT_BTN)
        dp.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DeleteProductLocators.EMPTY_BASKET_INFO))
