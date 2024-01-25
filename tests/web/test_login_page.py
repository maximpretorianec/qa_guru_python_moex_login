import pytest
import allure

from utils import TypeTag, Severity
from test_data import wrong_user_ui, user_ui
from pages.web import main, auth


@allure.epic('Страница авторизации')
class TestLoginPage:
    @allure.story('Авторизация на сайте')
    @allure.title('Авторизация на сайте успешна, на главной странице должен отображаться логин пользователя')
    @allure.feature('Авторизация')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    @pytest.mark.parametrize("login, pwd", [(user_ui.email, user_ui.password),
                                            (wrong_user_ui.email, wrong_user_ui.password)])
    def test_moex_login(self, login, pwd):
        main.open_core_site()
        main.click_cabinet_button_at_top_menu()

        auth.login(login, pwd)
        if login == user_ui.email:
            main.check_visibility_login_at_top_menu()
        else:
            main.check_visibility_login_alert()
