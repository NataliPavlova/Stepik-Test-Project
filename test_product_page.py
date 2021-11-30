from pages.product_page import ProductPage
import time
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


# @pytest.mark.parametrize('promo_offer',
#                          [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Normal')) for i in range(10)])

def test_guest_can_add_product_to_basket(browser):
    # link = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_offer))
    link = ProductPage.link
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера
    # и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину
    page.add_product_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # считаем результат математического выражения(alert) и вводим ответ,
    # что обеспечивает переход на другую страницуБ в корзину
    time.sleep(3)
    # product_page = ProductPage(browser, browser.current_url)
    page.should_be_correct_message_product_in_basket()  # проверяем, что товар добавился корректно
    # (наименование и цена совпают)
    # page.should_be_to_disappeared()  # проверяем, что сообщения об успешном добавлении в корзину пропадает


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPage.link
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = ProductPage.link
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPage.link
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_to_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(3)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_in_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
    basket_page.should_be_message_basket_empty()















