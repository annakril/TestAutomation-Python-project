from selenium.webdriver.common.by import By


class RodoLocators():
    RODO_POPUP = (By.XPATH, '//*[@id="rodo-popup"]')
    RODO_POPUP_ACCEPT_BTN = (By.XPATH, '//*[@class="button js-rodo-accept"]')


class SearchProductLocators():
    SEARCH_INPUT = (By.XPATH, '//*[@id="block-search-product-nav-input-text-search-world"]')
    SEARCHING_RESULT = (By.XPATH, '//*[@class="search-qty"]')


class SearchedProductLocators():
    FIRST_PRODUCT_LIST = (By.XPATH, '//*[@id="product_list"]/li[1]/div/div[2]/h5/a')
    PRODUCT_SEARCHED_LANDING_PAGE_ID = (By.CSS_SELECTOR, '#product_page_product_id')


class ChangeProductQuantityLocators():
    PRODUCT_PLUS_QUANTITY_BTN = (By.XPATH, '//*[@class="icon-plus"]')
    QUANTITY_VALUE = (By.CSS_SELECTOR, '#quantity_wanted')


class AddToBasketLocators():
    ADD_TO_BASKET_BTN = (By.XPATH, '//*[@id="add_to_cart"]/button')
    ADDED_TO_BASKET_CONFIRMATION_POPUP = (By.XPATH, '//*[@class="layer_cart_product__title"]')


class CompleteOrderLocators():
    REALIZUJ_ZAMOWIENIE_BTN = (By.XPATH, '//*[@class="pull-right button large high"]')
    BASKET_CART_TITLE = (By.XPATH, '//*[@id="cart_title"]')


class DeleteProductLocators():
    DELETE_PRODUCT_BTN = (By.XPATH, '//*[@class="icon-smietniczek"]')
    EMPTY_BASKET_INFO = (By.XPATH, '//*[@class="empty-cart-information"]')
