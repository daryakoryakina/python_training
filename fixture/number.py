import time

from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper
from model import number
from model.number import Number


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

    def fill_number_form(self, number):
        driver = self.app.driver
        self.change_field_value("firstname", number.first_name)
        self.change_field_value("middlename", number.middle_name)
        self.change_field_value("nickname", number.nickname)
        self.change_field_value("address2", number.address2)

    def click_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.XPATH, "//*[@title = 'Edit']")[index].click()

    def edit_number_by_index(self, index, number):
        driver = self.app.driver
        self.click_group_by_index(index)
        if len(driver.find_elements(By.NAME, "firstname")) > 0:
            self.change_field_value("firstname", number.first_name)
            self.change_field_value("nickname", number.nickname)
        driver.find_element(By.NAME, "update").click()
        self.number_cache = None

    def edit_number(self):
        self.edit_number_by_index(0)

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def delete_number(self):
        self.delete_number_by_index(0)

    def delete_number_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()
        driver.find_element(By.XPATH, "//input[@value = 'Delete']").click()
        driver.switch_to_alert().accept()
        self.number_cache = None

    def create_number(self, number):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//a[@href='edit.php']").click()
        self.fill_number_form(number)
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()
        self.number_cache = None

    def count(self):
        driver = self.app.driver
        self.open_number_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    number_cache = None

    def get_number_list(self):
        if self.number_cache is None:
            driver = self.app.driver
            self.open_number_page()
            self.number_cache = []
            for element in driver.find_elements(By.XPATH, "//*[@name='entry']"):
                cells = element.find_element(By.TAG_NAME, "td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                self.number_cache.append(Number(first_name=firstname, second_name=lastname, id=id))
            return list(self.number_cache)
