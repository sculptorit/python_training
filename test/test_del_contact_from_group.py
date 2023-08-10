import random

from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_del_contact_from_group(app):
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
    # выбираем случайный контакт
    rand_cont = random.choice(orm.get_contacts_not_in_group(rand_gr))
    # если нет группы с контактом, то добавляем контакт
    if len(orm.get_contacts_in_group(rand_gr)) == 0:
        app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
        assert rand_cont in orm.get_contacts_in_group(rand_gr)
    # выбираем случайный контакт для удаления из группы
    rand_cont_for_del = random.choice(orm.get_contacts_in_group(rand_gr))
    # удаляем контакт из группы
    app.contact.delete_contact_from_group_by_id(rand_cont_for_del.id, rand_gr.id)
    # проверка, что в списке групп с контактами появилась группа
    assert rand_cont_for_del not in orm.get_contacts_in_group(rand_gr)
    # проверка, что в списке групп без контактов группы нет
    assert rand_cont_for_del in orm.get_contacts_not_in_group(rand_gr)
