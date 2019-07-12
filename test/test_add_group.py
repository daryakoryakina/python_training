from sys import maxsize

import pytest

from data.add_group import testdata
from model.group import Group


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

# for name in ["", random_string("name", 5)]
# for header in ["", random_string("header", 10)]
# for footer in ["", random_string("footer", 10)]
