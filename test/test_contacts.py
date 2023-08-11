import re
from fixture.contact import Contact


def test_all_on_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_ui) == len(contacts_from_db)
    for i in range(len(contacts_from_ui)):
        assert contacts_from_ui[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_ui[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_ui[i].address == contacts_from_db[i].address
        assert contacts_from_ui[i].all_emails_from_home_page == merge_emails_like_on_homepage(contacts_from_db[i])
        assert contacts_from_ui[i].all_phones_from_home_page == merge_phone_like_on_homepage(contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phone_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))