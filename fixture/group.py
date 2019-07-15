from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper
from model.group import Group


class GroupHelper(BaseHelper):

    def create(self, group):
        driver = self.app.driver
        # click to create new group
        driver.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # click to creat group button
        driver.find_element(By.NAME, "submit").click()
        self.return_to_home_page()
        self.group_cache = None


    def click_to_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def click_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def open_group_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("group.php") and len(driver.find_elements(By.NAME, "new")) > 0):
            driver.find_element(By.XPATH, "//a[@href='group.php']").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.click_group_by_index(index)
        driver.find_element(By.NAME, "delete").click()
        self.group_cache = None

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def update_group(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//input[@value = 'Update']").click()
        self.group_cache = None

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_footer", group.footer)
        self.change_field_value("group_header", group.header)

    def edit_group_by_index(self, index, group):
        driver = self.app.driver
        self.click_group_by_index(index)
        driver.find_element(By.XPATH, "//input[@value = 'Edit group']").click()
        if driver.current_url.endswith("group.php") and len(driver.find_elements(By.NAME, "group_name")) > 0:
            self.fill_group_form(group)
            self.update_group()

    def edit_group(self):
        self.edit_group_by_index(0)

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//i/a[@href='group.php']").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_group_page()
            self.group_cache = []
            for element in driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)






