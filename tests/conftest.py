import pytest
import datetime
import allure
from selene import browser
from selenium import webdriver
from users.user import User
from selenium.webdriver.chrome.options import Options

from utils import attach

@pytest.fixture(autouse=True)
def browser_launch():
    with allure.step("Установка конфигурации драйвера"):
        options = Options()
        options.add_argument('--headless')
        selenoid_capabilities = {
            "browserName": "chrome",
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )

        browser.config.driver = driver
    # with allure.step("Установка настроек браузера"):
    #     browser.driver.set_window_size(1920, 1080)
    with allure.step("Открытие тестовой страницы"):
        browser.open('https://demoqa.com/automation-practice-form')
    yield
    with allure.step("Прикрепление данных к аллюр отчёту"):
        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_video(browser)
        attach.add_logs(browser)
    browser.close()


@pytest.fixture()
def create_user():
    return User(
        first_name='RandomName',
        last_name='RandomFamilyName',
        email='user@qa.com',
        gender='Male',
        mobile='9991111111',
        date_of_birth=datetime.date(1993, 9, 24),
        subject='Arts',
        hobby='Music',
        picture='Duck.jpg',
        address='Street',
        state='Uttar Pradesh',
        city='Lucknow'
    )
