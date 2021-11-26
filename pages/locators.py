from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_MESSAGE_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner strong')
    PRODUCT_PRICE_ELEMENT = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRODUCT_PRICE_MESSAGE_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) > .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1)')


