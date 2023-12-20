from selene.support.conditions import have, be
from selene.support.shared import browser
from utils.load_file import path
from users.user import User
import allure

class Registration:

    def register_user(self, user: User):
        with allure.step("Заполнение формы"):
            browser.execute_script("document.body.style.zoom='67%'")
            browser.element("#firstName").type(user.first_name)
            browser.element("#lastName").type(user.last_name)
            browser.element("#userEmail").type(user.email)
            browser.element("#userNumber").type(user.mobile)
            browser.element("#currentAddress").type(user.address)
            browser.element("#subjectsInput").type(user.subject).press_enter()
            browser.all('input[name=gender]').element_by(have.value(user.gender)).element('..').click()
            browser.all('.custom-checkbox').element_by(have.exact_text(user.hobby)).click()
            browser.element('#dateOfBirthInput').should(be.not_.blank).click()
            browser.element('.react-datepicker__month-select').type(user.date_of_birth.strftime('%B'))
            browser.element('.react-datepicker__year-select').type(user.date_of_birth.year)
            browser.element(
                f'.react-datepicker__day--0{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()
            browser.element("#uploadPicture").send_keys(path(user.picture))
            browser.element('#state').click()
            browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
            browser.element('#city').click()
            browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()

        with allure.step("Отправка формы"):
            browser.element('#submit').press_enter()

    def assert_registration_data(self, user: User):
        with allure.step("Проверка данных регистрации"):
            browser.element('.table').all('td').even.should(
                have.exact_texts(
                    f'{user.first_name} {user.last_name}',
                    user.email,
                    user.gender,
                    user.mobile,
                    user.date_of_birth.strftime('%d %B,%Y'),
                    user.subject,
                    user.hobby,
                    user.picture,
                    user.address,
                    f'{user.state} {user.city}',
                )
            )
