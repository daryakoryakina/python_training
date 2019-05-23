import time

from model.group import Group


def test_delete_first_group(app):
    app.open_page()
    if app.group.count(page="groups", endswith="/group.php", name="delete") == 0:
        app.group.create(Group(name="test"))
    app.group.click_to_first_group()
    app.group.delete_first_group()
    app.group.open_group_page()


