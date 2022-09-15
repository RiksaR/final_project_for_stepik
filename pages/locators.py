from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductLocators():
    BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (
        By.XPATH,
        "//div[@class='col-sm-6 product_main']/p[@class='price_color']"
    )
    PRODUCT_NAME_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
