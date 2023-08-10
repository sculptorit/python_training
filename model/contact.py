# -*- coding: utf-8 -*-
from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, email=None, email2=None, email3=None, address=None,  \
            all_emails_from_homepage=None, homephone=None, mobilephone=None, workphone=None, secondaryphone = None,  \
            all_phones_from_homepage = None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.firstname == other.firstname or self.firstname is None or other.firstname is None \
            and self.lastname == other.lastname or self.lastname is None or other.lastname is None

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
