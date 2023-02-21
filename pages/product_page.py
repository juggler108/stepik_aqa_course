from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button_and_add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()

    def should_be_message_added_to_basket_and_message_basket_price(self):
        self.should_be_message_added_to_basket()
        self.should_be_message_basket_price()

    def product_name_and_price_are_same_product_name_and_price_in_messages(self):
        self.product_name_is_same_product_name_in_message()
        self.product_price_is_same_basket_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET), \
            "No message about adding item to basket"

    def should_be_message_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_BASKET_PRICE), \
            "No message about basket price"

    def product_name_is_same_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name.text == product_name_in_message.text, \
            "The product name in the message does not match the name of the added product"

    def product_price_is_same_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert product_price.text == basket_price.text, \
            "The product price does not match with basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but it should have"
