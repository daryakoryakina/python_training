from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from model.group import Group


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    # открытие страницы адрессной книги
    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")


    def destroy(self):
        self.driver.quit()

