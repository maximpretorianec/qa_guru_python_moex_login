from .base_page import BasePage, step
from test_data import LocationsSchoolPage


class SchoolPage(BasePage):
    def check_visibility_moex_school_logo(self):
        with step('Иконка школы MOEX отображается в верхнем меню'):
            self.check_visibility(LocationsSchoolPage.moex_school_logo)
