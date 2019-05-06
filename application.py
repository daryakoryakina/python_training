from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

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

    def create_group(self, driver, group):
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

    def return_to_groups(self, driver):
        driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def test_login_type(self):
        driver = self.driver
        self.method_name(driver)
        self.login(driver, username="admin")
        self.password(driver, password="secret")
        self.open_groups(driver)
        self.create_group(driver, Group(group_name="zdfsdf", header="sdfzdfg", footer="zfgcfghcfh"))
        self.return_to_groups(driver)
        self.logout(driver)


    def destroy(self):
        self.driver.quit()

