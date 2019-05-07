from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper


class SessionHelper(BaseHelper):

# ввод логина
    def login(self, username, password):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element(By.XPATH, "//input[@name = 'user']").clear()
        driver.find_element(By.XPATH, "//input[@name = 'user']").send_keys(username)
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

# логаут
    def logout(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

# если на странице есть элемент Логаут, то делать логаут

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element(By.XPATH, "//*[text() ='(admin)']").text == "("+username+")"








