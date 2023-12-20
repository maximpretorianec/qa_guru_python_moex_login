from pages.Registration import Registration


def test_form(create_user):
    registration_page = Registration()

    registration_page.register_user(create_user)

    registration_page.assert_registration_data(create_user)
