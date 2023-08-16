import random

from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_del_con_from_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # pre check
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New contact"))
    groups_orm = orm.get_group_list()
    rand_gr = random.choice(groups_orm)
    rand_cont = random.choice(orm.get_contacts_not_in_group(rand_gr))
    # preaction - precheck2
    if len(orm.get_contacts_in_group(rand_gr)) == 0:
        app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
        assert rand_cont in orm.get_contacts_in_group(rand_gr)
    rand_cont_for_del = random.choice(orm.get_contacts_in_group(rand_gr))
    app.contact.delete_contact_from_group_by_id(rand_cont_for_del.id, rand_gr.id)
    #fincheck
    assert rand_cont_for_del not in orm.get_contacts_in_group(rand_gr)
    assert rand_cont_for_del in orm.get_contacts_not_in_group(rand_gr)