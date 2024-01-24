from .base_page import BasePage, step
from test_data import LocationsMainPage


class MainPage(BasePage):
    def __init__(self):
        with step('Открыть главную страницу'):
            self.open_site('/')

    def check_visibility_moex_icon(self):
        with step('Проверка отображения лого MOEX в верхнем меню'):
            self.check_visibility(LocationsMainPage.moex_logo)

    def check_visibility_lang_switch_at_top_menu(self):
        with step('Проверка отображения перключения языков в верхнем меню'):
            self.check_visibility(LocationsMainPage.lang_section)

    def check_visibility_search_at_top_menu(self):
        with step('Проверка отображения поиска в верхнем меню'):
            self.check_visibility(LocationsMainPage.search_field)

    def check_visibility_cabinet_button_at_top_menu(self):
        with step('Проверка отображения входа в верхнем меню'):
            self.check_visibility(LocationsMainPage.login_field)

    def check_visibility_cart_button_at_top_menu(self):
        with step('Проверка отображения корзины в верхнем меню'):
            self.check_visibility(LocationsMainPage.cart_button)

    def click_cabinet_button_at_top_menu(self):
        with step('Нажатие кнопки входа'):
            self.click_button(LocationsMainPage.login_field)

    def check_visibility_login_at_top_menu(self, login):
        with step('Имя пользователя отображается в верхнем меню'):
            self.check_visibility(LocationsMainPage(login).login_field_by_user_text)

    def click_login_at_top_menu(self, login):
        with step('Нажатие кнопки личного кабинета пользователя'):
            self.click_button(LocationsMainPage(login).login_field_by_user_text)

    def click_logout_at_top_menu(self):
        with step('Выход из системы'):
            self.click_button(LocationsMainPage.logout_field)

    def click_href(self, link_href):
        with step('Открыть раздел обучения'):
            self.click_button(LocationsMainPage(link_href).page_href_by_text)

    def check_rus_name_at_top_menu(self, rus_text):
        with step('В верхнем меню отображаются элементы на русском языке'):
            self.check_visibility(LocationsMainPage(rus_text).header_obj_with_text)

    def check_eng_name_at_top_menu(self, eng_text):
        with step('В верхнем меню отображаются элементы на английском языке'):
            self.check_visibility(LocationsMainPage(eng_text).header_obj_with_text)

    def click_switch_lang_at_top_menu(self):
        with step('Переключение языков'):
            self.click_button(LocationsMainPage.switch_lang_button)

    def click_remove_product_from_cart(self):
        with step('Удалить продукт из корзины'):
            self.click_button(LocationsMainPage.remove_product_button)

    def check_remove_product_from_cart(self):
        with step('Проверка корзины, после удаления'):
            return self.is_visibility_element(LocationsMainPage.remove_product_button)

    def click_empty_cart_button_at_top_menu(self):
        with step('Открыть пустую корзину'):
            self.click_button(LocationsMainPage.empty_cart_button)

    def click_add_service_to_cart_button(self):
        with step('Добавить продукты в корзину'):
            self.click_button(LocationsMainPage.add_product_button)

    def click_filling_cart_button_at_top_menu(self):
        with step('Открыть заполненную корзину'):
            self.click_button(LocationsMainPage.filling_cart_button)

    def check_visibility_filling_cart(self):
        with step('Проверка отображения заполненной корзины'):
            self.check_visibility(LocationsMainPage.filling_cart_section)
