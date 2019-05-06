
from model.newnum import NewNum


def test_add_contact(app):
    app.open_page()
    app.session.login(username="admin")
    app.session.password(password="secret")
    app.number.type_firstname(NewNum(first_name="dfggtxf", middle_name="edszertgderxde", nickname="fgxhgcfj", address2="sdfzdfgxdhgcfj"))
    app.number.click_save()
    app.session.logout()


