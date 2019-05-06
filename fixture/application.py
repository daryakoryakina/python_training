from selenium import webdriver
from selenium.webdriver.common.by import By

from model.group import Group


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def login(self, username):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name = 'user']").click()
        driver.find_element(By.XPATH, "//input[@name = 'user']").clear()
        driver.find_element(By.XPATH, "//input[@name = 'user']").send_keys(username)

    def password(self, password):
        driver = self.driver
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()


    def open_groups(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        driver = self.driver
        # click to create new group
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.group_name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # click to creat group button
        driver.find_element(By.NAME, "submit").click()

    def return_to_groups(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def test_login_type(self):
        self.open_page()
        self.login(username="admin")
        self.password(password="secret")
        self.open_groups()
        self.create_group(Group(group_name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
        self.return_to_groups()
        self.logout()


    def destroy(self):
        self.driver.quit()

