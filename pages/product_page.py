from pages.base_page import BasePage
from locators import ChangeProductQuantityLocators
from locators import AddToBasketLocators
from locators import CompleteOrderLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def change_quantity_plus(self):
        qp = self.driver.find_element(*ChangeProductQuantityLocators.PRODUCT_PLUS_QUANTITY_BTN)
        qp.click()

    def add_to_basket(self):
        ab = self.driver.find_element(*AddToBasketLocators.ADD_TO_BASKET_BTN)
        ab.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AddToBasketLocators.ADDED_TO_BASKET_CONFIRMATION_POPUP))

    def go_to_basket(self):
        rz = self.driver.find_element(*CompleteOrderLocators.REALIZUJ_ZAMOWIENIE_BTN)
        rz.click()
