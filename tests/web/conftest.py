import pytest
import allure

from selene import browser
from utils import attach
from test_data import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='module', autouse=True)
def browser_launch():
    with allure.step("Установка настроек браузера"):
        browser.driver.set_window_size(1920, 1080)
        browser.config.base_url = 'https://www.moex.com/'
    yield
    with allure.step("Прикрепление данных к аллюр отчёту"):
        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_video(browser)
        attach.add_logs(browser)
    browser.quit()
