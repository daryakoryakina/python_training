from model.group import Group


def test_group_list(db):
    #web_list = app.group.get_group_list()
    db_list = db.get_group_list()
    return print(db_list)
    # assert sorted(web_list, key=Group.id_or_max) == sorted(db_list)