# -*- coding: utf-8 -*-
from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home = home
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.firstname == other.firstname or self.firstname is None or other.firstname is None \
            and self.lastname == other.lastname or self.lastname is None or other.lastname is None

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
