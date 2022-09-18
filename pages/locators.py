from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FOR_REGISTRATION = (By.ID, 'id_registration-email')
    PASSWORD_FOR_REGISTRATION = (By.ID, 'id_registration-password1')
    REPASSWORD_FOR_REGISTRATION = (By.ID, 'id_registration-password2')
    BUTTON_FOR_REGISTRATION = (
        By.CSS_SELECTOR,
        "button[name='registration_submit']"
    )


class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (
        By.XPATH,
        "//div[@class='col-sm-6 product_main']/p[@class='price_color']"
    )
    PRODUCT_NAME_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
