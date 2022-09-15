from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-" \
           f"handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.checking_the_product_name()
    page.checking_the_price_of_the_goods()
