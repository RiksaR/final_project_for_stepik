from .pages.product_page import ProductPage
import pytest
from .pages.login_page import LoginPage

# params = list(map(str, range(10)))
#
# @pytest.mark.parametrize('param', [
#     x if x != '7' else pytest.param(x, marks=pytest.mark.xfail) for x in params
# ])
# def test_guest_can_add_product_to_basket(browser, param):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_" \
#            f"207/?promo=offer{param}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.checking_the_product_name()
#     page.checking_the_price_of_the_goods()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-' \
#            f'work_207/'
#     page = ProductPage(browser, link, 0)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-' \
#            f'work_207/'
#     page = ProductPage(browser, link, 0)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-' \
#            f'work_207/'
#     page = ProductPage(browser, link, 0)
#     page.open()
#     page.add_to_basket()
#     page.should_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-" \
           "and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-" \
           "and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
