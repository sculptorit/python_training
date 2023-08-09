# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="rdgr", lastname="erge", address="erger", home="ergerg",
                                email="regergerg")
    contact.id = old_contacts[0].id
    app.contact.mod_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_mod_first_contact_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="rdgr")
#    app.contact.mod_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
