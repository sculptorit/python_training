from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_full_contact_info(self, contact):
        wd = self.app.wd
        self.to_add_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_info(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.to_home_page()
        self.contact_cache = None

    def fill_contact_info(self, contact):
        self.fill_contacts(contact)
        self.fill_phones(contact)
        self.fill_personal_info(contact)
        self.fill_dates(contact)
        self.fill_secondary_info(contact)

    def fill_contacts(self, contact):
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def fill_phones(self, contact):
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)

    def fill_personal_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

    def fill_dates(self, contact):
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_secondary_info(self, contact):
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.get(self.app.base_url+"index.php")

    def to_add_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get(self.app.base_url+"edit.php")

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        self.delete_some_contact(0)

    def delete_some_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.some_edit_by_index(index)
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def delete_some_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.some_edit_by_id(id)
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def first_edit(self):
        self.some_edit_by_index(0)

    def some_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def some_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='%s']/../..//*[@title='Edit']" % id).click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(new_contact_data, 0)

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.some_edit_by_index(index)
        self.fill_contact_info(new_contact_data)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        self.to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.some_edit_by_id(new_contact_data.id)
        self.fill_contact_info(new_contact_data)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        self.to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                addr = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=addr, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_page(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname,
                       id=id, address=address, home=homephone, work=workphone,
                       mobile=mobilephone, phone2=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_page(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone,
                       mobile=mobilephone, phone2=secondaryphone)

    def add_contact_to_group_by_id(self, cont_id, gr_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(cont_id)
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % gr_id).click()
        wd.find_element_by_css_selector("input[value='Add to']").click()

    def delete_contact_from_group_by_id(self, cont_id, gr_id):
        wd = self.app.wd
        self.app.open_home_page()
        #селект из списка
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % gr_id).click()
        wd.implicitly_wait(5)
        self.select_contact_by_id(cont_id)
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()
