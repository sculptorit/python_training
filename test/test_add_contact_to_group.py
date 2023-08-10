import random

from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_add_contact_to_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # если нет контактов, создаем контакт
    if len(orm.get_contact_list()) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    # если нет группы, создаем группу
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="New first group"))
    # список групп
    groups_orm = orm.get_group_list()
    # выбираем случайную группу
    rand_gr = random.choice(groups_orm)
    # список контактов, у кого нет группы
    contacts_not_in_group_list = orm.get_contacts_not_in_group(rand_gr)
    # если нет контактов не в группе, то создаем контакт ещё раз
    if len(contacts_not_in_group_list) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
        contacts_not_in_group_list = orm.get_contacts_not_in_group(rand_gr)
    # выбираем случайный контакт из тех, у кого нет группы
    rand_cont = random.choice(contacts_not_in_group_list)
    # добавляем контакт в группу
    app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
    # добавить ассерты
    assert rand_cont in orm.get_contacts_in_group(rand_gr)
