import time

from model.group import Group


def test_edit_group(app):
    app.open_page()
    app.group.edit_group(Group(name="123456766"))  # header="123456789", footer="123456789"))
    app.group.return_to_groups()

