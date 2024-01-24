import allure

from utils import TypeTag, Severity
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
        login_page.login()
        main_page.open_product_catalog()

        prod_page = ProductPage()
        prod_page.fill_product_to_cart()
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
        login_page.login()
        main_page.open_product_catalog()

        prod_page = ProductPage()
        prod_page.fill_product_to_cart()
        main_page.remove_product_from_cart()

        main_page.is_assert_equal_memory(main_page.check_remove_product_from_cart(), False)
