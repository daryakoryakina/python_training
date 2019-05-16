from model.number import Number


def test_edit_contact(app):
    app.open_page()
    app.number.edit_number(Number(second_name="1234567", nickname="123456", address2="ffgxdhxfjx", middle_name="fgdzsxhgcxfjh", first_name="sgfdxzdhxf"))


