# import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # l = db.get_contact_list()
    # l = db.get_contacts_in_group(Group(id='1'))
    l = db.get_contacts_in_group(Group(id='64'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
