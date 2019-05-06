import time

def test_delete_contact(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.number.delete_number()
    app.session.logout()
