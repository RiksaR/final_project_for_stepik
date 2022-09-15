from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductLocators.BUTTON).click()

    def checking_the_product_name(self):
        prod_name = self.browser.find_element(
            *ProductLocators.PRODUCT_NAME
        ).text
        prod_name_in_basket = self.browser.find_element(
            *ProductLocators.PRODUCT_NAME_IN_BASKET
        ).text
        assert prod_name == prod_name_in_basket,\
            f'The product name in the catalog and the shopping cart must match'

    def checking_the_price_of_the_goods(self):
        prod_price = self.browser.find_element(
            *ProductLocators.PRODUCT_PRICE
        ).text
        prod_price_in_basket = self.browser.find_element(
            *ProductLocators.PRODUCT_PRICE_IN_BASKET
        ).text
        assert prod_price == prod_price_in_basket, \
            f'The price of the product in the catalog and the basket must match'
