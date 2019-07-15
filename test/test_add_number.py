import pytest

from data.numbers import testdata
from model.number import Number


@pytest.mark.parametrize("number", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_number):
    number = json_number
    app.open_page()
    app.number.open_number_page()
    old_number = app.number.get_number_list()
    app.number.create_number(number)
    assert len(old_number) + 1 == app.number.count()
    new_number = app.number.get_number_list()
    old_number.append(number)
    assert sorted(old_number, key=Number.id_or_max) == sorted(new_number, key=Number.id_or_max)


# for firstname in ["", random_string("firstname", 5)]
# for lastname in ["", random_string("lastname", 10)]
# for address in ["", random_string("address", 10)]
# for company in ["", random_string("company", 10)]