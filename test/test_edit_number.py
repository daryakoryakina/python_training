from random import randrange

from model.number import Number


def test_edit_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create_number(Number(firstname="testtest"))
    old_number = app.number.get_number_list()
    index = randrange(len(old_number))
    number = Number(lastname="1234567", firstname="sgfdxzdhxf")
    number.id = old_number[index].id
    app.number.edit_number_by_index(index, number)
    new_number = app.number.get_number_list()
    assert len(old_number) == len(new_number)
    old_number[index] = number
    assert sorted(old_number, key=Number.id_or_max) == sorted(new_number, key=Number.id_or_max)
