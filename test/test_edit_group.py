import time

from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_group(Group(name="123456766"))  # header="123456789", footer="123456789"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

