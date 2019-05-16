from model.group import Group


def test_delete_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create(Group(name="test"))
    app.number.delete_number()

