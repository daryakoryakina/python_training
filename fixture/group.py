from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper


class GroupHelper(BaseHelper):


    def create(self, group):
        driver = self.app.driver
        # click to create new group
        driver.find_element_by_name("new").click()
        # fill group form
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_footer", group.footer)
        self.change_field_value("group_header", group.header)
        # click to creat group button
        driver.find_element(By.NAME, "submit").click()

    def click_to_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def open_group_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("group.php") and len(driver.find_elements(By.NAME, "new")) > 0):
            driver.find_element(By.XPATH, "//a[@href='group.php']").click()

    def delete_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "delete").click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def update_group(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//input[@value = 'Update']").click()

    def edit_group(self, group):
        driver = self.app.driver
        self.click_to_first_group()
        driver.find_element(By.XPATH, "//input[@value = 'Edit group']").click()
        if driver.current_url.endswith("group.php") and len(driver.find_elements(By.NAME, "group_name")) > 0:
            self.change_field_value("group_name", group.name)
            self.change_field_value("group_footer", group.footer)
            self.change_field_value("group_header", group.header)
            self.update_group()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//i/a[@href='group.php']").click()




