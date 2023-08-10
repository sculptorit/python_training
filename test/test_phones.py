import re
from fixture.contact import Contact


def test_phones_on_homepage(app, db):
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_ui)):
        assert contacts_from_ui[i].all_phones_from_home_page == merge_phone_like_on_homepage(contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def test_phones_on_viewpage(app):
    contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_viewpage.homephone == contact_from_edit_page.homephone
    assert contact_from_viewpage.workphone == contact_from_edit_page.workphone
    assert contact_from_viewpage.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_viewpage.secondaryphone == contact_from_edit_page.secondaryphone


def merge_phone_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondaryphone]))))
