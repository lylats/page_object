from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что в адресе страницы есть "login"
        assert "/login" in self.browser.current_url, 'word "login" not in url'

    def should_be_login_form(self):
        # проверка наличия формы логин
        assert self.is_element_present(*LoginPageLocators.LOGIN_FROM), "login form is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"

    def register_new_user(self, email, password):
        # вызыв функции для проверка наличия формы регистрации на странице
        # self.should_be_register_form()

        # находим элементы на странице: поля ввода почты, пароля и кнопку регистрации
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        # вводим почту, пароль
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)

        # нажимаем на кнопку: зарегистрировать
        register_button.click()
