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

    def edit_number(self, number):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//*[@title = 'Edit']").click()
        self.change_field_value("firstname", number.first_name)
        self.change_field_value("nickname", number.nickname)
        driver.find_element(By.NAME, "update").click()
        driver.find_element(By.LINK_TEXT, "home page").click()

    def home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def delete_number(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.XPATH, "//input[@value = 'Delete']").click()
        driver.switch_to_alert().accept()

    def create_number(self, number):
        driver = self.app.driver
        self.change_field_value("firstname", number.first_name)
        self.change_field_value("middlename", number.middle_name)
        self.change_field_value("nickname", number.nickname)
        self.change_field_value("address2", number.address2)
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()










