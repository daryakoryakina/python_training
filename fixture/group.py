from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper


class GroupHelper(BaseHelper):

    def open(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        driver = self.app.driver
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
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

0