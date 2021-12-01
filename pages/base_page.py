from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        # открытие станицы браузера
        self.browser.get(self.url)

    def go_to_login_page(self):
        # переход на страницу логина
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        # проверка, что ссылка на страницу логина есть
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        # проверка, что элемент есть на странице (how - как ищем, what - что ищем)
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # проверяем, что элемент не появляется на странице в течение заданного времени (timeout=4)
        # упадет, как только увидит искомый элемент; не появился (timeout): успех, тест зеленый
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

    def is_disappeared(self, how, what, timeout=4):
        # проверяем, что элемент исчезает
        # будет ждать до тех пор, пока элемент не исчезнет; упадет, если через timeout элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        # метод для решение математического alert (расчет формулы и ввод ответа)
        # WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_in_basket(self):
        # переход в корзину по кнопке в шапке сайта
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()

    def should_be_authorized_user(self):
        # проверка, что пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     "probably unauthorised user"