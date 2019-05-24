
from model.number import Number


def test_add_contact(app):
    app.open_page()
    app.base.open(page="add new", endswith="/edit.php", name="firstname")
    app.number.create_number(Number(second_name="dgfxdghcfghm", first_name="dfggtxf", middle_name="edszertgderxde", nickname="fgxhgcfj", address2="sdfzdfgxdhgcfj"))
    app.number.home_page()



