
from model.group import Group


def test_login_type(app):
    app.open_page()
    app.group.open(page="groups", endswith="/group.php", name="new")
    app.group.create(Group(name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    app.group.open_group_page()



