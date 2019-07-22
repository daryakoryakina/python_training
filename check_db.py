import pymysql.connections

from fixture.orm import ORMfixture

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")
#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cont = db.get_number_list()
    for con in cont:
        print(con)
    print(len(cont))
    # cursor = connection.cursor()
    # cursor.execute("select 'May' from month_lookup")
    # for row in cursor.fetchall():
        # print(row)
finally:
    pass