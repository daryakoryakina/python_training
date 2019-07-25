from random import randrange

from model.number import Number


def test_edit_contact(app, db):
    app.open_page()
    if db.get_number_list() == 0:
        app.number.create_number(Number(firstname="testtest"))
    old_number = db.get_number_list()
    index = randrange(len(old_number))
    number = Number(lastname="1234567", firstname="sgfdxzdhxf")
    number.id = old_number[index].id
    app.number.edit_number_by_index(index, number)
    new_number = db.get_number_list()
    assert len(old_number) == len(new_number)
    old_number[index] = number
    assert sorted(old_number, key=Number.id_or_max) == sorted(new_number, key=Number.id_or_max)


# dictionary = {'os':'windows', 'os_virsion':8.1}
# dictionary['os']

