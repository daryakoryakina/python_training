from random import randrange

from model.number import Number


def test_delete_some_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create_number(Number(first_name="testtest"))
    old_number = app.number.get_number_list()
    index = randrange(len(old_number))
    app.number.delete_number_by_index(index)
    new_number = app.number.get_number_list()
    assert len(old_number) - 1 == len(new_number)
    old_number[index:index+1] = []
    assert old_number == new_number


