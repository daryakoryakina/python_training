import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fixture.base_fixture import BaseHelper

from model.number import Number

import re


class NumberHelper(BaseHelper):

    # метод для изменения одного параметра
    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def open_number_page(self):
        driver = self.app.driver
        if not (len(driver.find_elements(By.NAME, "add")) > 0):
            driver.find_element(By.XPATH, "//a[@href='./' and contains(text(), 'home')]").click()

    def fill_number_form(self, number):
        driver = self.app.driver
        self.change_field_value("firstname", number.firstname)
        self.change_field_value("lastname", number.lastname)
        self.change_field_value("nickname", number.nickname)
        self.change_field_value("address2", number.address2)
        self.change_field_value("company", number.company)
        self.change_field_value("address", number.address)
        self.change_field_value("email", number.email)
        self.change_field_value("email2", number.email2)
        self.change_field_value("home", number.homephone)
        self.change_field_value("mobile", number.mobilephone)
        self.change_field_value("work", number.workphone)
        self.change_field_value("phone2", number.email2)


    def click_number_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.XPATH, "//*[@title = 'Edit']")[index].click()


    def edit_number_by_index(self, index, number):
        driver = self.app.driver
        self.click_number_by_index(index)
        self.fill_number_form(number)
        driver.find_element(By.NAME, "update").click()
        self.number_cache = None

    def edit_number(self):
        self.edit_number_by_index(0)

    def select_group(self, group_id):
        driver = self.app.driver
        group = Select(driver.find_element(By.NAME, "to_group"))
        group.select_by_value('%s' % group_id)
        driver.find_element(By.XPATH, "//input[@value = 'Add to']").click()



    def add_number_in_group(self, group_id):
        driver = self.app.driver
        driver.find_element(By.ID, "MassCB").click()
        self.select_group(group_id)


    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def delete_number(self):
        self.delete_number_by_index(0)

    def delete_number_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()
        driver.find_element(By.XPATH, "//input[@value = 'Delete']").click()
        driver.switch_to_alert().accept()
        self.number_cache = None

    def create_number(self, number):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//a[@href='edit.php']").click()
        self.fill_number_form(number)
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()
        self.number_cache = None
        self.return_to_home_page()

    def count(self):
        driver = self.app.driver
        self.open_number_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    number_cache = None

    def get_number_list(self):
        if self.number_cache is None:
            driver = self.app.driver
            self.open_number_page()
            self.number_cache = []
            for element in driver.find_elements(By.XPATH, "//*[@name = 'entry']"):
                cells = element.find_elements(By.XPATH, "//tr/td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.number_cache.append(
                    Number(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones,
                           address=address, all_emails=all_emails))
        return list(self.number_cache)

    def open_number_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_number_page()
        row = driver.find_elements(By.XPATH, "//*[@name = 'entry']")[index]
        cell = row.find_elements(By.XPATH, "//tr/td")[3]
        cell.find_element(By.XPATH, "//*[@title = 'Edit']").click()

    def open_number_view_by_index(self, index):
        driver = self.app.driver
        self.open_number_page()
        row = driver.find_elements(By.XPATH, "//*[@name = 'entry']")[index]
        row.find_element(By.XPATH, "//*[@title = 'Details']").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_number_to_edit_by_index(index)
        firstname = driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = driver.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = driver.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = driver.find_element(By.NAME, "work").get_attribute("value")
        secondaryphone = driver.find_element(By.NAME, "phone2").get_attribute("value")
        address = driver.find_element(By.NAME, "address").get_attribute("value")
        email = driver.find_element(By.NAME, "email").get_attribute("value")
        email2 = driver.find_element(By.NAME, "email2").get_attribute("value")
        return Number(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                      workphone=workphone, secondaryphone=secondaryphone,
                      address=address, email=email, email2=email2)

    def get_number_from_view_page(self, index):
        driver = self.app.driver
        self.open_number_view_by_index(index)
        text = driver.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Number(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def delete_number_by_id(self, id):
        driver = self.app.driver
        self.click_number_by_id(id)
        driver.find_element(By.XPATH, "//input[@value = 'Delete']").click()
        driver.switch_to_alert().accept()
        self.number_cache = None

    def click_number_by_id(self, id):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//input[@value='%s']" % id).click()

    def delete_number_from_group(self, group_id):
        driver = self.app.driver
        group = Select(driver.find_element(By.NAME, "group"))
        group.select_by_value('%s' % group_id)
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.XPATH, "//input[@name='remove']").click()









