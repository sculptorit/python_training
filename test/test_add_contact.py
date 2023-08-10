# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fghjk", lastname="fghnjmk",
                      homephone="12323232121", mobilephone="79121232221", workphone="79531232221", secondaryphone="79324354221",
                    email="test@mail.ru",email_2="test2@mail.ru", email_3="test3@mail.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
