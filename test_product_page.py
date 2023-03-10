import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = LoginPage(browser, link)
        page.open()

        page.should_be_login_link()
        page.go_to_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "abcdefg"

        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button_and_add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_added_to_basket_and_message_basket_price()
        page.product_name_and_price_are_same_product_name_and_price_in_messages()


@pytest.mark.need_review
# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])
@pytest.mark.parametrize('link', [0])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button_and_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_added_to_basket_and_message_basket_price()
    page.product_name_and_price_are_same_product_name_and_price_in_messages()


@pytest.mark.xfail
# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@pytest.mark.parametrize('link', [0])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button_and_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@pytest.mark.parametrize('link', [0])
def test_guest_cant_see_success_message(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@pytest.mark.parametrize('link', [0])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button_and_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@pytest.mark.parametrize('link', [0])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    basket_page = BasketPage(browser, link)
    basket_page.is_not_products_in_basket()
    basket_page.should_be_empty_basket_message()
