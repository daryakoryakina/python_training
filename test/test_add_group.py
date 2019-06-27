
from model.group import Group


def test_open_group(app):
    app.open_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    app.open_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)




