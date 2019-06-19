
from model.group import Group


def test_open_group(app):
    app.open_page()
    app.group.open_group_page()
    app.group.create(Group(name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    app.group.open_group_page()



