# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_first_contact(app):
    app.contact.mod_first_contact(Contact(firstname="rdgr", lastname="erge", address="erger", home="ergerg",
                                email="regergerg"))


def test_mod_first_contact_name(app):
    app.contact.mod_first_contact(Contact(firstname="rdgr"))
