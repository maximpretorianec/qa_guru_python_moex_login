import allure

from utils import TypeTag, Severity
from test_data import MoexVariables
from pages.web import MainPage, LoginPage


@allure.epic('Главная страница')
class TestMainPage:
    @allure.story('Открыть главную страницу')
    @allure.title('Стартовая страница, проверка базовых элементов страницы')
    @allure.feature('Главная страница')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.SMOKE, TypeTag.REGRESS, TypeTag.UI, Severity.CRITICAL)
    @allure.severity(Severity.CRITICAL)
    def test_open_main_page(self):
        main_page = MainPage()

        main_page.check_visibility_moex_icon()
        main_page.check_visibility_cabinet_button_at_top_menu()
        main_page.check_visibility_cart_button_at_top_menu()
        main_page.check_visibility_lang_switch_at_top_menu()
        main_page.check_visibility_search_at_top_menu()

    @allure.story('Выход из системы')
    @allure.title('Выход из системы, на главной странице снова доступен вход')
    @allure.feature('Выход из системы')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MINOR)
    @allure.severity(Severity.MINOR)
    def test_moex_logout(self):
        main_page = MainPage()
        main_page.click_cabinet_button_at_top_menu()

        login_page = LoginPage()
        login_page.login()
        main_page.logout()

        main_page.check_visibility_cabinet_button_at_top_menu()

    @allure.story('Смена языков')
    @allure.title('Должен смениться язык на странице на английский')
    @allure.feature('Смена языков')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.TRIVIAL)
    @allure.severity(Severity.TRIVIAL)
    def test_switch_language(self):
        main_page = MainPage()
        main_page.check_rus_name_at_top_menu(MoexVariables.rus_text)

        main_page.click_switch_lang_at_top_menu()
        main_page.check_eng_name_at_top_menu(MoexVariables.eng_text)
