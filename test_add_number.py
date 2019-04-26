# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from newnum import NewNum
from pages.group_page import GroupPage


class TestAddContact(unittest.TestCase, GroupPage):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/addressbook/")

    def auth(self, driver, username, password):
        group_page = GroupPage(driver)
        group_page.login(driver, username)
        group_page.password(driver, password)
        group_page.auth_click(driver)

    def type_firstname(self, newnum):
        self.driver.find_element_by_link_text("add new").click()

        self.driver.find_element_by_name("firstname").clear()
        self.driver.find_element_by_name("firstname").send_keys(newnum.first_name)
        self.driver.find_element_by_name("middlename").clear()
        self.driver.find_element_by_name("middlename").send_keys(newnum.middle_name)
        self.driver.find_element_by_name("nickname").clear()
        self.driver.find_element_by_name("nickname").send_keys(newnum.nickname)
        self.driver.find_element_by_name("address2").clear()
        self.driver.find_element_by_name("address2").send_keys(newnum.address2)

    def click_save(self):
        self.driver.find_element_by_xpath("//input[@value='Enter']").click()
        self.driver.find_element_by_link_text("home page").click()

    def logout(self, driver):
        group_page = GroupPage(driver)
        group_page.click_on(self.LOGOUT)

    def test_add_contact(self):
        driver = self.driver
        self.auth(driver, username="admin", password="secret")
        self.type_firstname(NewNum(first_name="dfggtxf", middle_name="edszertgderxde", nickname="fgxhgcfj", address2="sdfzdfgxdhgcfj"))
        self.click_save()
        self.logout(driver)


if __name__ == "__main__":
    unittest.main()
