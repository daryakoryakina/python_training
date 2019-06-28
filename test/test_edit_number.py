from model.number import Number


def test_edit_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create_number(Number(first_name="testtest"))
    old_number = app.number.get_number_list()
    number = Number(second_name="1234567", first_name="sgfdxzdhxf")
    number.id = old_number[0].id
    app.number.edit_number(number)
    new_number = app.number.get_number_list()
    assert len(old_number) == len(new_number)
    old_number[0] = number
    assert sorted(old_number, key=Number.id_or_max) == sorted(new_number, key=Number.id_or_max)



