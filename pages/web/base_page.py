from selene import browser, be
from allure import step


class BasePage:
    def open_main_page(self):
        with step('Открыть стартовую страницу'):
            browser.open('/')

    def pikabu_icon_at_top_menu_should_be_visible(self):
        with step('Иконка пикабу отображается в верхнем меню'):
            browser.element('#icon icon--ui__pikabu')

    def open_best_tab(self):
        with step('Открыть кладку Сообщества'):
            browser.element('#menu-communities').should(be.visible).click()

    def check_create_communities_button(self):
        with step('Найти кнопку создания сообщества'):
            browser.element('a[href$="/communities/add"]').should(be.visible)

    def check_all_communities_string(self):
        with step('Найти строку - все сообщества'):
            browser.element('a[href$="/communities"]').should(be.visible)

    def click_on_auth(self):
        with step('нажать войти'):
            browser.element('.auth__field.auth__field_firstbtn').should(be.visible)

    def check_login_input(self):
        with step('Найти поле для ввода логина'):
            browser.element('[name=username]').should(be.visible)

    def check_pwd_input(self):
        with step('Найти поле для ввода пароля'):
            browser.element('[name=password]').should(be.visible)

    def remove_advertisement(self):
        with step('Скрыть рекламу'):
            ind, loc = self.find_attr_advertisement()
            if loc:
                browser.element(loc).execute_script('element.remove()')
                if ind == 'vk':
                    browser.element('[data-test-id=floatingOneTap]').execute_script('element.remove()')

    def find_attr_advertisement(self):
        with step('Проверка наличия рекламы'):
            type_ad = {'yandex': 'iframe[src*=yandex]', 'vk': 'iframe[src*=vk]'}
            for ind, val in type_ad.items():
                if browser.element(val).wait_until(be.visible):
                    return ind, val
            return None, None
