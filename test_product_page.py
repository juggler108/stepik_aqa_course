from time import sleep

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_added_to_basket()
    page.should_be_message_basket_price()
    page.is_true_name_product_in_message()
    page.product_price_is_same_basket_price()
