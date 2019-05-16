from model.number import Number


def test_edit_contact(app):
    app.open_page()
    app.number.edit_number(Number(second_name="1234567", first_name="sgfdxzdhxf"))


