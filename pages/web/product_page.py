from .base_page import BasePage, step
from test_data import LocationsProductPage


class ProductPage(BasePage):
    def click_subscribe_button(self):
        with step('Нажатие на подписку хода торгов'):
            self.click_button(LocationsProductPage.cource_trading_subs)

    def select_residence_choice_button(self):
        with step('Выбрать резиденство РФ'):
            self.click_button(LocationsProductPage.rus_residence)

    def click_approve_residence_choice_button(self):
        with step('Подтверждение резиденства'):
            self.click_button(LocationsProductPage.approve_residence)

    def select_product_by_button(self):
        with step('Выбрать продукт по подписке хода торгов'):
            self.click_button(LocationsProductPage.trade_product)

    def click_fill_cart_button(self):
        with step('Добавление в корзину'):
            self.click_button(LocationsProductPage.filling_cart_button)
