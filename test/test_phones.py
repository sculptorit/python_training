import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phone_like_on_homepage(contact_from_edit_page)


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
                                filter(lambda x: x is not None, [contact.homephone, contact.workphone,
                                                                 contact.mobilephone, contact.secondaryphone]))))
