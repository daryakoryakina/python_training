from model.group import Group


def test_group_list(app, db):
    web_list = app.group.get_group_list()
    db_list = db.get_group_list()
    assert sorted(web_list) == sorted(db_list)