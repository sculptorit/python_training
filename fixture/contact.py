import re
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("aday")) > 0 and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[21]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        # self.go_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='%s']/../..//*[@title='Edit']" % id).click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.go_to_home_page()
        # open contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit mod
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.go_to_home_page()
        # open contact
        self.select_contact_by_id(id)
        self.fill_contact_form(new_contact_data)
        # submit mod
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def go_to_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0 and len(wd.find_elements_by_name("to_group")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for cell in wd.find_elements_by_name("entry"):
                id = cell.find_element_by_name("selected[]").get_attribute("value")
                firstname = cell.find_element_by_xpath("td[3]").text
                lastname = cell.find_element_by_xpath("td[2]").text
                address = cell.find_element_by_xpath("td[4]").text
                all_emails = cell.find_element_by_xpath("td[5]").text
                all_phones = cell.find_element_by_xpath("td[6]").text
                self.contact_cache.append(Contact( id=id, firstname=firstname, lastname=lastname, address=address, all_emails_from_homepage=all_emails, all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")[7]
        cells.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")[6]
        cells.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       email = email, email2 = email2, email3 = email3)

    def get_contact_from_viewpage(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)