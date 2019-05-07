import time

def test_delete_contact(app):
    app.open_page()
    app.number.delete_number()

