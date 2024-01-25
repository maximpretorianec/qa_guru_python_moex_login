Предусловия:
- Установить зависимости из файла requirements.txt 
- Создать файл .env, в корне проекта, с указанием след переменных(для зарегистрированных пользователей):
  - AUTHORIZATION_LOGIN
  - AUTHORIZATION_PASSWORD

- Установить allure для генерации отчётов на локальной машине - https://github.com/allure-framework/allure2


Запуск:
- всего проекта:
    pytest -sv
- конкретных тестов:
  - pytest *путь до файла с тестами*::*класс*::*название теста* -sv --alluredir=allure-results --clean-alluredir
  - пример:
    - pytest tests/web/test_login_page.py::TestLoginPage::test_moex_login -sv --alluredir=allure-results --clean-alluredir

Посмотреть отчётность:
- allure serve tests/web/allure-results(Для отчётов по web)
- allure serve(Для отчётов по всем тестам)
