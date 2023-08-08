# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_first_group(app):
    app.group.modify_first_group(Group(name="wef", header="wee", footer="wegew"))


def test_mod_group_name(app):
    app.group.modify_first_group(Group(name="wef"))


def test_mod_group_header(app):
    app.group.modify_first_group(Group(header="wee"))
