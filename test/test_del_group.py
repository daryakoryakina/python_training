
def test_delete_first_group(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.group.delete_first_group()
    app.group.return_to_groups()
    app.session.logout()

