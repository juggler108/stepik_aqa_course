from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".page_inner .alertinner strong")
    MESSAGE_WITH_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info")

    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    GO_TO_BASKET = (By.CSS_SELECTOR, "span a.btn")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_FREE_ELEMENT = (By.CSS_SELECTOR, "#content_inner>p")

