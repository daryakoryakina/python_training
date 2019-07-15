import pymysql.connections

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select 'May' from month_lookup")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()