from model.number import Number


def test_delete_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create_number(Number(first_name="testtest"))
    old_number = app.number.get_number_list()
    app.number.delete_number()
    new_number = app.number.get_number_list()
    assert len(old_number) - 1 == len(new_number)
    old_number[0:1] = []
    assert old_number == new_number



