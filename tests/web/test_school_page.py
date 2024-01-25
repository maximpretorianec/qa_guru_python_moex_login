import allure

from utils import TypeTag, Severity
from test_data import MoexUrl
from pages.web import main, school


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
        main.open_core_site()
        main.open_new_tab_school()

        school.check_visibility_moex_school_logo()
        school.is_assert_equal_values(MoexUrl.SCHOOL_URL, school.get_curr_url())
