from datetime import datetime

from pony.orm import *

from model.group import Group
from model.number import Number


class ORMfixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        numbers = Set(lambda: ORMfixture.ORMNumber, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMNumber(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMfixture.ORMGroup, table="address_in_groups", column="group_id",
                     reverse="numbers", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, autocommit=True)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMfixture.ORMGroup))

    def convert_numbers_to_model(self, number):
        def convert(number):
            return Number(id=str(number.id), firstname=number.firstname, lastname=number.lastname)

        return list(map(convert, number))

    @db_session
    def get_number_list(self):
        return self.convert_numbers_to_model(select(c for c in ORMfixture.ORMNumber if c.deprecated is None))

    @db_session
    def get_numbers_in_group(self, group):
        orm_group = list(select(g for g in ORMfixture.ORMGroup if g.id == group.id))[0]
        return self.convert_numbers_to_model(orm_group.numbers)

    @db_session
    def get_numbers_not_in_group(self, group):
        orm_group = list(select(g for g in ORMfixture.ORMGroup if g.id == group.id))[0]
        return self.convert_numbers_to_model(
            select(c for c in ORMfixture.ORMNumber if c.deprecated is None and orm_group not in c.groups))



