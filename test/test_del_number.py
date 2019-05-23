from model.number import Number


def test_delete_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create(Number(first_name="testtest"))
    app.number.delete_number()

