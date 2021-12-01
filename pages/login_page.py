from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        # проверка, что на странице логина есть:
        self.should_be_login_url()  # корректный url адрес
        self.should_be_login_form()  # форма логина
        self.should_be_register_form()  # форма регистрации

    def should_be_login_url(self):
        # проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login register form is not presented"
        assert True

    def register_new_user(self, email, password):
        # регистрация нового пользователя (заполнение формы регистрации)
        email_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_registration.send_keys(email)

        password_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_registration.send_keys(password)

        confirm_password_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        confirm_password_registration.send_keys(password)

        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()








