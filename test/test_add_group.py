
from model.group import Group


def test_login_type(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.group.open()
    app.group.create(Group(group_name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
    app.group.return_to_groups()
    app.session.logout()
