# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_mod_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fghjk", lastname="fghnjmk",
                          homephone="12323232121", mobilephone="79121232221", workphone="79531232221",
                          secondaryphone="79324354221",
                          email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="change", lastname="change",
                          homephone="79121232221", mobilephone="79531232221", workphone="79324354221",
                          secondaryphone="79121232221",
                          email="test11@mail.ru", email2="test22@mail.ru", email3="test33@mail.ru")
    app.contact.modify_contact_by_index(contact, index)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)