import allure

from utils import TypeTag, Severity
from pages.web import MainPage, LoginPage


@allure.epic('Страница авторизации')
class TestLoginPage:
    @allure.story('Авторизация на сайте')
    @allure.title('Авторизация на сайте успешна, на главной странице должен отображаться логин пользователя')
    @allure.feature('Авторизация')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_moex_login(self):
        main_page = MainPage()
        main_page.click_cabinet_button_at_top_menu()

        login_page = LoginPage()
        login_page.login()

        main_page.check_visibility_login_at_top_menu()
