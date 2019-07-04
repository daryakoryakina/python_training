
from model.number import Number


def test_add_contact(app):
    app.open_page()
    app.number.open_number_page()
    old_number = app.number.get_number_list()
    number = Number(firstname="dfggtxf", lastname="dfhxfkjvghk", nickname="fgxhgcfj", address2="sdfzdfgxdhgcfj")
    app.number.create_number(number)
    assert len(old_number) + 1 == app.number.count()
    new_number = app.number.get_number_list()
    old_number.append(number)
    assert sorted(old_number, key=Number.id_or_max) == sorted(new_number, key=Number.id_or_max)

