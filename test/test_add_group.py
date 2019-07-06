from sys import maxsize

import pytest

from model.group import Group
import random
import string


# генератор случайных данных
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 5)]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]
    ]


# перед параметризированным тестом ставится такая метка
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_open_group(app, group):
    app.open_page()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
