import allure

from utils import TypeTag, Severity
from test_data import auth_email, auth_password
from pages.web import MainPage, LoginPage, ProductPage


@allure.epic('Страница продуктов Мосбиржи')
class TestProdPage:
    @allure.story('Добавление продуктов в корзину')
    @allure.title('Продукты должны быть добавлены в корзину и отображаться')
    @allure.feature('Добавление продуктов в корзину')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_fill_cart(self):
        main_page = MainPage()
        main_page.click_cabinet_button_at_top_menu()
        login_page = LoginPage()
        login_page.type_login_form(auth_email)
        login_page.type_password_form(auth_password)
        login_page.btn_login_click()
        main_page.click_empty_cart_button_at_top_menu()
        main_page.click_add_service_to_cart_button()

        prod_page = ProductPage()
        prod_page.click_subscribe_button()
        prod_page.select_residence_choice_button()
        prod_page.click_approve_residence_choice_button()
        prod_page.select_product_by_button()
        prod_page.click_fill_cart_button()
        main_page.click_filling_cart_button_at_top_menu()
        main_page.check_visibility_filling_cart()

    @allure.story('Очистка корзины')
    @allure.title('После удаления продуктов, корзина должна быть пустой')
    @allure.feature('Очищение корзины')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_remove_product_from_cart(self):
        main_page = MainPage()
        main_page.click_cabinet_button_at_top_menu()
        login_page = LoginPage()
        login_page.type_login_form(auth_email)
        login_page.type_password_form(auth_password)
        login_page.btn_login_click()
        main_page.click_empty_cart_button_at_top_menu()
        main_page.click_add_service_to_cart_button()

        prod_page = ProductPage()
        prod_page.click_subscribe_button()
        prod_page.select_residence_choice_button()
        prod_page.click_approve_residence_choice_button()
        prod_page.select_product_by_button()
        prod_page.click_fill_cart_button()
        main_page.click_filling_cart_button_at_top_menu()
        main_page.click_remove_product_from_cart()
        main_page.is_assert_equal_memory(main_page.check_remove_product_from_cart(), False)
