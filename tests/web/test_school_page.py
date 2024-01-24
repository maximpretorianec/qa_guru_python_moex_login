import allure

from utils import TypeTag, Severity
from test_data import MoexUrl
from pages.web import MainPage, SchoolPage


@allure.epic('Страница обучения')
class TestSchoolPage:
    @allure.story('Открытие раздела сайта - Обучение')
    @allure.title('Страница обучения должна быть открыта в новой вкладке')
    @allure.feature('Страница обучения')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MINOR)
    @allure.severity(Severity.MINOR)
    def test_open_school_tab(self):
        main_page = MainPage()
        main_page.click_href(MoexUrl.SCHOOL_URL)
        main_page.switch_tab()
        school_page = SchoolPage()
        school_page.check_visibility_moex_school_logo()
        school_page.is_assert_equal_values(MoexUrl.SCHOOL_URL, school_page.get_curr_url())
