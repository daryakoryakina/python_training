
from model.group import Group


def test_login_type(app):
    app.open_page()
    app.group.open()
    app.group.create(Group(name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    app.group.return_to_groups()


def test_login_type_2(app):
    app.open_page()
    app.group.open()
    app.group.create(Group(name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    app.group.return_to_groups()


