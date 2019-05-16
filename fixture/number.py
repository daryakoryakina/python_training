import time

from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper
from model import number


class NumberHelper(BaseHelper):

    def open_contact(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    # метод для изменения одного параметра
    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def fill_number_form(self, number):
        driver = self.app.driver
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(number.first_name)
        driver.find_element(By.NAME, "middlename").clear()
        driver.find_element(By.NAME, "middlename").send_keys(number.middle_name)
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys(number.nickname)
        driver.find_element(By.NAME, "address2").clear()
        driver.find_element(By.NAME, "address2").send_keys(number.address2)

    def click_save(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()

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





