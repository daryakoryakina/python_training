import pymysql

from model.group import Group
from model.number import Number


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=id, name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_number_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Number(id=id, firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_number_by_id(self, num_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where "
                           "deprecated='0000-00-00 00:00:00' and id='%s' % number_id")
            for row in cursor:
                (id, firstname, lastname) = row
                num_id = (Number(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return num_id

    def destroy(self):
        self.connection.close()
