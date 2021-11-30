from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        # проверяем (ожидаем), что в корщине нет тоаров (корзина пуста)
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty"
        assert True

    def should_be_message_basket_empty(self):
        message_element = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_NON_PRODUCT)
        message = message_element.text
        assert 'Your basket is empty' in message, "Check your basket"






