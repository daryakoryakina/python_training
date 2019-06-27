
from model.number import Number


def test_add_contact(app):
    app.open_page()
    app.number.open_number_page()
    old_number = app.number.get_number_list()
    app.number.create_number(Number(second_name="dgfxdghcfghm", first_name="dfggtxf", middle_name="edszertgderxde", nickname="fgxhgcfj", address2="sdfzdfgxdhgcfj"))
    new_number = app.number.get_number_list()
    app.number.return_to_home_page()
    assert len(old_number) +1 == len(new_number)



