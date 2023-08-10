import re
from fixture.contact import Contact


def test_phones_on_home_page(app, db):
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_ui)):
        assert contacts_from_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


# проверка информации о контактах на главной странице
def test_all_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_full_contact_info(Contact(firstname="New first firstname"))
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_ui) == len(contacts_from_db)
    for i in range(len(contacts_from_ui)):
        assert contacts_from_ui[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_ui[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_ui[i].address == contacts_from_db[i].address
        assert contacts_from_ui[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
        assert contacts_from_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
