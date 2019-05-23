from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper
from fixture.group import GroupHelper
from fixture.number import NumberHelper
from fixture.session import SessionHelper
from model.group import Group


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.number = NumberHelper(self)
        self.base = BaseHelper(self)

    # открытие страницы адрессной книги
    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    # закрытие
    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False
