from pages.base_page import BasePage
from locators import RodoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AcceptRodoPage(BasePage):
    def accept_rodo(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RodoLocators.RODO_POPUP))
        rp = self.driver.find_element(*RodoLocators.RODO_POPUP_ACCEPT_BTN)
        rp.click()
