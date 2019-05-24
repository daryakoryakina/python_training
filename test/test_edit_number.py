from model.number import Number


def test_edit_contact(app):
    app.open_page()
    if app.base.count(page="home", endswith="/edit.php?id=38", name="update") == 0:
        app.number.create_number(Number(first_name="testtest"))
    app.number.edit_number(Number(second_name="1234567", first_name="sgfdxzdhxf"))


