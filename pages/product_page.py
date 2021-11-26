from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_message_product_in_basket(self):
        # проверяем совпадает ли название товара и цена в сообщении (в корзине) с тем,что мы добавили
        product_name = self.product_name()
        product_name_in_basket = self.message_product_name_in_basket()
        self.should_be_correct_message_product_name_in_basket(product_name, product_name_in_basket)

        product_price = self.product_price()
        product_price_in_basket = self.message_product_price_in_basket()
        self.should_be_correct_message_product_price_in_basket(product_price, product_price_in_basket)

    def product_name(self):
        #  фиксируем (возвращаем) название товара  из карточки товара, добавляемого в корзину
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name_element.text
        return product_name

    def message_product_name_in_basket(self):
        # находим сообщение, что товар добавлен и фиксруем название товара в сообщении
        product_name_element_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE_IN_BASKET)
        product_name_in_basket = product_name_element_in_basket.text
        return product_name_in_basket

    def should_be_correct_message_product_name_in_basket(self, product_name, product_name_in_basket):
        # проверяем совпадают ли названия товара, который добавили в корзину с названием в сообщении
        # для проверки наименование товара передаютя в качестве параметров
        # product_name = self.product_name()
        # product_name_in_basket = self.message_product_name_in_basket()
        assert product_name == product_name_in_basket, "Non"

    # аналогично и с ценой
    def product_price(self):
        product_price_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ELEMENT)
        product_price = product_price_el.text
        return product_price

    def message_product_price_in_basket(self):
        product_price_el_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE_IN_BASKET)
        product_price_in_basket = product_price_el_in_basket.text
        return product_price_in_basket

    def should_be_correct_message_product_price_in_basket(self, product_price, product_price_in_basket):
        # product_price = self.product_price()
        # product_price_in_basket = self.message_product_price_in_basket()
        assert product_price == product_price_in_basket, 'Non'







