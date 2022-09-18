from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON).click()

    def checking_the_product_name(self):
        prod_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        prod_name_in_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET
        ).text
        assert prod_name == prod_name_in_basket, \
            f'The product name in the catalog and the shopping cart must match'

    def checking_the_price_of_the_goods(self):
        prod_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        prod_price_in_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_BASKET
        ).text
        assert prod_price == prod_price_in_basket, \
            f'The price of the product in the catalog and the basket must match'

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message must is disappeared, but it present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
