import re


def test_email_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phone_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


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