from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fghjk", lastname="fghnjmk", address="hggkygyug",
                          homephone="12323232121", mobilephone="79121232221", workphone="79531232221",
                          secondaryphone="79324354221",
                          email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
