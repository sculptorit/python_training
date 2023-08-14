import pymysql.connections
from model.group import Group
from model.contact import Contact


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
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, "
                           "homephone, mobilephone, workphone, seconphone from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, homephone, mobilephone, workphone,
                 secondphone) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, home=homephone,
                                    mobile=mobilephone, work=workphone, address=address, email=email,
                                    email2=email2, email3=email3, secondphone=secondphone))
        finally:
            cursor.close()
        return list


    def get_contacts_not_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT addressbook.id, addressbook.firstname, addressbook.lastname "
                           "FROM  addressbook where addressbook.id not in ( select addressbook.id "
                           "FROM  address_in_groups INNER JOIN addressbook "
                           "ON addressbook.id = address_in_groups.id "
                           "WHERE addressbook.deprecated = '0000-00-00 00:00:00' "
                           "AND address_in_groups.deprecated = '0000-00-00 00:00:00' "
                           "AND address_in_groups.group_id = '%s')" % group_id)

            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group_list(self, group):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where group_id='%s'" % group)
            for row in cursor:
                (id, group_id) = row
                list.append({'id': str(id), 'group_id': str(group_id)})
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
