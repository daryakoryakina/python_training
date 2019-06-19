import time

from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper
from model import number


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

    def edit_number(self, number):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//*[@title = 'Edit']").click()
        if len(driver.find_elements(By.NAME, "firstname")) > 0:
            self.change_field_value("firstname", number.first_name)
            self.change_field_value("nickname", number.nickname)
        driver.find_element(By.NAME, "update").click()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()


    def delete_number(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.XPATH, "//input[@value = 'Delete']").click()
        driver.switch_to_alert().accept()

    def create_number(self, number):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//a[@href='edit.php']").click()
        self.change_field_value("firstname", number.first_name)
        self.change_field_value("middlename", number.middle_name)
        self.change_field_value("nickname", number.nickname)
        self.change_field_value("address2", number.address2)
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()

    def count(self):
        driver = self.app.driver
        self.open_number_page()
        return len(driver.find_elements(By.NAME, "selected[]"))










