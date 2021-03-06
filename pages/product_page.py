from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        # добавление товара в корзину
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_message_product(self):
        # проверяем совпадает ли название товара и цена в сообщении, что товар добавлен в корзину
        product_name = self.product_name()
        product_name_in_basket = self.message_product_name()
        self.should_be_correct_message_product_name(product_name, product_name_in_basket)

        product_price = self.product_price()
        product_price_in_basket = self.message_product_price()
        self.should_be_correct_message_product_price(product_price, product_price_in_basket)

    def should_not_be_success_message(self):
        # сообщения об успешном добавлении товара в корзину не должно быть на странице товара
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_to_disappeared(self):
        # проверка, что элемент (сообщение об успешном добавлении товара в корзнину) исчезает
        # по проекту не должно исчезать
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should"

    def product_name(self):
        #  фиксируем (возвращаем) название товара  из карточки товара, добавляемого в корзину
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name_element.text
        return product_name

    def message_product_name(self):
        # находим сообщение, что товар добавлен и фиксруем название товара в сообщении
        product_name_element_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE)
        product_name_in_basket = product_name_element_in_basket.text
        return product_name_in_basket

    def should_be_correct_message_product_name(self, product_name, product_name_in_basket):
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

    def message_product_price(self):
        product_price_el_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE)
        product_price_in_basket = product_price_el_in_basket.text
        return product_price_in_basket

    def should_be_correct_message_product_price(self, product_price, product_price_in_basket):
        # product_price = self.product_price()
        # product_price_in_basket = self.message_product_price_in_basket()
        assert product_price == product_price_in_basket, 'Non'







