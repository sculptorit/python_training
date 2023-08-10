# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = Group(name="New group").name
    app.group.modify_group_by_id(group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
