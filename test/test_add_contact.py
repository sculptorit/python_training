# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="fghjk", lastname="fghnjmk", address="fghjk", home="bnm",
                                email="vbn"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", home="", email=""))

