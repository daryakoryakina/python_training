from model.group import Group


def test_edit_group(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.group.edit_group(Group(group_name="1234567", header="123456789", footer="123456789"))
    app.group.return_to_groups()
    app.session.logout()