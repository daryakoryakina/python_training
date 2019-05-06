from model.edit_num import EditNum


def test_edit_contact(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.number.edit_number(EditNum(second_name="1234567", nickname="123456"))
    app.session.logout()

