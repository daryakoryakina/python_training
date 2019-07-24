import random

from model.number import Number


def test_delete_some_contact(app, db, check_ui):
    app.open_page()
    if len(db.get_number_list()) == 0:
        app.number.create_number(Number(firstname="testtest"))
    old_number = db.get_number_list()
    number = random.choice(old_number)
    app.number.delete_number_by_id(number.id)
    new_number = db.get_number_list()
    assert len(old_number) - 1 == len(new_number)
    old_number.remove(number)
    assert old_number == new_number
    if check_ui:
        assert sorted(new_number, key=Number.id_or_max) == sorted(app.number.get_number_list(), key=Number.id_or_max)
