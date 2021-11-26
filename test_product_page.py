from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('promo_offer',
                         # [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Normal')) for i in range(10)
                          [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Normal')) for i in range(1)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'
            .format(promo_offer))
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
    page.should_be_to_disappeared()  # проверяем, что сообщения об успешном добавлении в корзину пропадает

