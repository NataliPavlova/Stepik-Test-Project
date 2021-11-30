from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера
        # и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # переход в корзину с главной страницы по ссылке в шапке сайта
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()  # открываем главную страницу
    page.go_to_in_basket()  # переходим по ссылки (кнопке) в корзину
    basket_page = BasketPage(browser, browser.current_url)  # переходим на страницу корзины
    basket_page.should_be_basket_empty()  # проверяем (ожидаем), что в корзине нет товаров
    basket_page.should_be_message_basket_empty()  # проверяем, что есть сообщение, что корзина пуста






















