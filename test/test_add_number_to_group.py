import random

from fixture.orm import ORMfixture
from model.group import Group
from model.number import Number

db = ORMfixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_number_in_group(app, db):
    app.open_page()
    if db.get_number_list() == 0:
        app.number.create_number(Number(firstname="testtest"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = db.get_group_list()
    group_id = random.choice(group).id
    app.number.add_number_in_group(group_id)
