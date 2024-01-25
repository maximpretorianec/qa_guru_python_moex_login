from utils import BaseActions, step
from test_data import LocationsLoginPage, user_ui


class LoginPage(BaseActions):
    def type_login_form(self, login):
        with step('Ввод логина'):
            self.type_text(LocationsLoginPage.login_field, login)

    def type_password_form(self, password):
        with step('Ввод пароля'):
            self.type_text(LocationsLoginPage.password_field, password)

    def btn_login_click(self):
        with step('Нажатие кнопки "войти"'):
            self.click_button(LocationsLoginPage.enter_button)

    def login(self, login=user_ui.email, password=user_ui.password):
        with step('Авторизация на сайте'):
            self.type_login_form(login)
            self.type_password_form(password)
            self.btn_login_click()


auth = LoginPage()
