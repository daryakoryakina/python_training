from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from contact import LoginGroup
from group import Group


class GroupTest(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def method_name(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        group_page = LoginGroup()
        group_page.USER_FIELD.clear()
        group_page.USER_FIELD.send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        # click to create new group
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # click to creat group button
        wd.find_element_by_name("submit").click()

    def return_to_groups(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_login_type(self):
        wd = self.wd
        self.method_name(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups(wd)
        self.create_group(wd, Group(group_name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
        self.return_to_groups(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
