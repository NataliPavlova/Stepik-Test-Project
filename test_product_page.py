from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Normal')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_offer))
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_correct_message_product_in_basket()
    time.sleep(3)

