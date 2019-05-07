from model.edit_num import EditNum


def test_edit_contact(app):
    app.open_page()
    app.number.edit_number(EditNum(second_name="1234567", nickname="123456"))


