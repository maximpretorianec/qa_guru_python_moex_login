class LocationsLoginPage:
    login_field = 'input.form-control[type="text"]'
    password_field = 'input.form-control[type="password"]'
    enter_button = 'button[type="submit"]'


class LocationsProductPage:
    cource_trading_subs = '#course_trading_subscribe'
    rus_residence = '//input[@value="1"]/ancestor::label[2]'
    approve_residence = '//button[contains(., "Ok")]'
    trade_product = '//input[contains(@id, "orderProduct")]/ancestor::label[1]'
    filling_cart_button = '//button[contains(., "В корзину")]'


class LocationsMainPage:
    moex_logo = '.header__logo .nuxt-link-exact-active .app-logo img'
    lang_section = '.lang-switch'
    search_field = 'label[for=moex-search-input] svg'
    login_field = '.cabinet-text a[href*="#"]'
    logout_field = '.cabinet-text_logout'
    cart_button = '.cart-button'
    switch_lang_button = '//span[contains(@class, "lang-switch__lang") and not(contains(@class, "lang-switch__lang--active"))]'
    remove_product_button = 'div.shopping-cart-wrapper tbody button'
    empty_cart_button = 'button[aria-label="Открыть корзину"]'
    add_product_button = 'div.shopping-cart-footer .base-button--primary'
    filling_cart_button = '.cabinet__auth button[aria-label="Открыть корзину"]'
    filling_cart_section = 'div.shopping-cart-wrapper tbody'
    alert_mess = '.alert-error'

    def __init__(self, text):
        self.login_field_by_user_text = f'//div[@class="cabinet-button"]/span[contains(., "{text}")]'
        self.page_href_by_text = f'a[href*="{text}"].site-header-menu__top-link'
        self.header_obj_with_text = f'//ul[@class="site-header-menu__main-list"]/*[contains(.,"{text}")]'


class LocationsSchoolPage:
    moex_school_logo = '.nuxt-link-exact-active div'
