import random

from fixture.orm import ORMfixture
from model.group import Group
from model.number import Number

# orm = ORMfixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_number_in_group(app, db, orm):
    app.open_page()
    if db.get_number_list() == 0:
        app.number.create_number(Number(firstname="testtest"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    app.group.open_group_page()
    group = db.get_group_list()
    group_id = random.choice(group).id
    number_id = random.choice(orm.get_numbers_in_group(Group(id=group_id))).id
    app.number.delete_number_from_group(group_id)
    app.number.add_number_in_group(group_id)
    assert db.get_number_by_id(number_id) not in orm.get_numbers_in_group(Group(id=group_id))
