from selenium import webdriver


from fixture.base_fixture import BaseHelper
from fixture.group import GroupHelper
from fixture.number import NumberHelper
from fixture.session import SessionHelper
from model.group import Group


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.number = NumberHelper(self)
        self.base = BaseHelper(self)
        self.base_url = base_url

    # открытие страницы адрессной книги
    def open_page(self):
        driver = self.driver
        driver.get(self.base_url)

    # закрытие
    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
