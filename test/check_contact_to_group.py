import random
from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_contact_to_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    #pre check
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Tech group"))
    if len(orm.get_contact_list()) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="Tech firstname"))
    groups_orm = orm.get_group_list()
    rand_gr = random.choice(groups_orm)
    #free contacts
    contacts_not_in_group_list = orm.get_contacts_not_in_group(rand_gr)
    #pre action (pre check 2)
    if len(contacts_not_in_group_list) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="Tech firstname"))
        contacts_not_in_group_list = orm.get_contacts_not_in_group(rand_gr)
    rand_cont = random.choice(contacts_not_in_group_list)
    app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
    #final check
    assert rand_cont in orm.get_contacts_in_group(rand_gr)
    assert rand_cont not in orm.get_contacts_not_in_group(rand_gr)