from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from application import Application
from group import Group
from pages.group_page import GroupPage


class GroupTest(unittest.TestCase, GroupPage):

    def setUp(self):
        self.app = Application()


    def login(self, driver, username):
        group_page = GroupPage(driver)
        group_page.click_on(self.USER_FIELD)
        group_page.clear_input(self.USER_FIELD)
        group_page.type_in(self.USER_FIELD, username)

    def password(self, driver, password):
        group_page = GroupPage(driver)
        group_page.clear_input(self.PASS_FIELD)
        group_page.type_in(self.PASS_FIELD, password)
        group_page.click_on(self.AUTH_BUTTON)

    def open_groups(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()



    def test_login_type(self):
        driver = self.driver
        self.app.method_name(driver)
        self.login(driver, username="admin")
        self.password(driver, password="secret")
        self.open_groups(driver)
        self.create_group(driver, Group(group_name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
        self.return_to_groups(driver)
        self.logout(driver)


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
