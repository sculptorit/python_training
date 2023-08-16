# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fghjk", lastname="fghnjmk",
                          homephone="12323232121", mobilephone="79121232221", workphone="79531232221",
                          secondaryphone="79324354221",
                          email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = Contact(firstname="newnewnew").firstname
    app.contact.modify_contact_by_id(contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
