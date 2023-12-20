import pytest
import datetime
from selene import browser
from users.user import User


@pytest.fixture(autouse=True)
def browser_launch():
    browser.driver.set_window_size(1920, 1080)
    browser.open('https://demoqa.com/automation-practice-form')
    yield
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
