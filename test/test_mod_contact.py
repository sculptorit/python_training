# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.mod_first_contact(Contact(firstname="rdgr", lastname="erge", address="erger", home="ergerg",
                                email="regergerg"))
    app.session.logout()
