import allure

from utils import TypeTag, Severity
from pages.web import main, auth, prod


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
        main.open_core_site()
        main.click_cabinet_button_at_top_menu()

        auth.login()
        main.open_product_catalog()

        prod.fill_product_to_cart()
        main.click_filling_cart_button_at_top_menu()

        main.check_visibility_filling_cart()

    @allure.story('Очистка корзины')
    @allure.title('После удаления продуктов, корзина должна быть пустой')
    @allure.feature('Очищение корзины')
    @allure.label('owner', 'mgolubev')
    @allure.label('layer', TypeTag.UI)
    @allure.tag(TypeTag.REGRESS, TypeTag.UI, Severity.MAJOR)
    @allure.severity(Severity.MAJOR)
    def test_remove_product_from_cart(self):
        main.open_core_site()
        main.click_cabinet_button_at_top_menu()

        auth.login()
        main.open_product_catalog()

        prod.fill_product_to_cart()
        main.remove_product_from_cart()

        main.is_assert_equal_memory(main.check_remove_product_from_cart(), False)
