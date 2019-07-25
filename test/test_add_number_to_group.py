import random
from model.group import Group
from model.number import Number


def test_add_number_in_group(app, orm):
    app.open_page()
    if orm.get_number_list() == 0:
        app.number.create_number(Number(firstname="testtest"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = orm.get_group_list()
    group_id = random.choice(group).id
    app.number.add_number_in_group(group_id)

