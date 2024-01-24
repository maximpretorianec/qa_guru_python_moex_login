from utils import BaseActions, step
from test_data import LocationsSchoolPage


class SchoolPage(BaseActions):
    def check_visibility_moex_school_logo(self):
        with step('Иконка школы MOEX отображается в верхнем меню'):
            self.check_visibility(LocationsSchoolPage.moex_school_logo)
