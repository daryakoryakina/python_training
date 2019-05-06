from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper


class SessionHelper(BaseHelper):

# ввод логина
    def login(self, username):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element(By.XPATH, "//input[@name = 'user']").click()
        driver.find_element(By.XPATH, "//input[@name = 'user']").clear()
        driver.find_element(By.XPATH, "//input[@name = 'user']").send_keys(username)

# атомарный ввод пароля и неатомарный клик на кнопку входа
    def password(self, password):
        driver = self.app.driver
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

# логаут
    def logout(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()