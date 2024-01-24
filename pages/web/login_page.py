from .base_page import BasePage, step
from test_data import LocationsLoginPage


class LoginPage(BasePage):
    def type_login_form(self, login):
        with step('Ввод логина'):
            self.type_text(LocationsLoginPage.login_field, login)

    def type_password_form(self, password):
        with step('Ввод пароля'):
            self.type_text(LocationsLoginPage.password_field, password)

    def btn_login_click(self):
        with step('Нажатие кнопки "войти"'):
            self.click_button(LocationsLoginPage.enter_button)
