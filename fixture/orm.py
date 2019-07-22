from datetime import datetime

from pony.orm import *
from pymysql.converters import decoders

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

    class ORMNumber(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, autocommit=True, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMfixture.ORMGroup))

    @db_session
    def get_number_list(self):
        return self.convert_numbers_to_model(select(c for c in ORMfixture.ORMNumber if c.deprecated is None))

    def convert_numbers_to_model(self, number):
        def convert(number):
            return Number(id=str(number.id), firstname=number.firstname, lastname=number.lastname)
        return list(map(convert, number))



