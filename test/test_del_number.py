from model.number import Number


def test_delete_contact(app):
    app.open_page()
    if app.base.count(page="add new", endswith="/edit.php", name="firstname") == 0:
        app.number.create(Number(first_name="testtest"))
    app.number.delete_number()

