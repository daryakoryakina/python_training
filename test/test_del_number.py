import time

from model.number import Number


def test_delete_contact(app):
    app.open_page()
    if app.number.count() == 0:
        app.number.create_number(Number(first_name="testtest"))
    time.sleep(10)
    app.number.delete_number()

