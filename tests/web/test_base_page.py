import allure

from pages.web.base_page import BasePage


@allure.epic('Стартовая страница')
class TestBasePage:
    @allure.story('Открыть стартовую страницу')
    @allure.title('Стартовая страница, иконка сайта должна отображаться')
    @allure.feature('Стартовая страница')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    def test_open_base_page(self):
        base_page = BasePage()

        base_page.open_main_page()
        base_page.pikabu_icon_at_top_menu_should_be_visible()

    @allure.story('Открыть вкладу "Сообщества"')
    @allure.title('Вкладка "Сообщества" должна отображаться')
    @allure.feature('Сообщества')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    def test_open_best_tab(self):
        base_page = BasePage()

        base_page.open_main_page()
        base_page.open_best_tab()
        base_page.check_create_communities_button()
        base_page.check_all_communities_string()

    @allure.story('Проверка панели авторизации')
    @allure.title('Панель авторизации должна отображаться')
    @allure.feature('Панель авторизации')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('regress', 'web', 'normal')
    @allure.severity('normal')
    def test_open_auth_form(self):
        base_page = BasePage()

        base_page.open_main_page()
        base_page.click_on_auth()
        base_page.check_login_input()
        base_page.check_pwd_input()
