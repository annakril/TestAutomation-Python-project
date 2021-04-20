class DataBase():
    url = 'https://drogeriapigment.pl/'
    executable_path = r'C:\Users\akril\PycharmProjects\chromedriver.exe'


class DataRodo():
    expected_rodo_pop_up_state_displayed = 'display: none;'


class DataProduct():
    invalid_product_name = 'ąóę'
    valid_product_name = 'lynia'
    expected_invalid_searching_result_text = '(0 PRODUKTÓW)'
    expected_quantity_value = '2'


class DataBasket():
    expected_added_to_basket_confirmation_pop_up_text = 'produkt został dodany do koszyka'
    expected_cart_title_basket_text = 'koszyk'
    expected_empty_basket_info_text = 'Twój koszyk jest pusty'
