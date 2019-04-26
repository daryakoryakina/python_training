from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GroupPage(BasePage):
    USER_FIELD = (By.XPATH, "//input[@name = 'user']")
    PASS_FIELD = (By.NAME, "pass")
    AUTH_BUTTON = (By.XPATH, "//input[@value='Login']")
    LOGOUT = (By.LINK_TEXT, "Logout")

    def login(self, driver, username):
        group_page = GroupPage(driver)
        group_page.click_on(self.USER_FIELD)
        group_page.clear_input(self.USER_FIELD)
        group_page.type_in(self.USER_FIELD, username)

    def password(self, driver, password):
        group_page = GroupPage(driver)
        group_page.clear_input(self.PASS_FIELD)
        group_page.type_in(self.PASS_FIELD, password)

    def auth_click(self, driver):
        group_page = GroupPage(driver)
        group_page.click_on(self.AUTH_BUTTON)

    def logout(self, driver):
        group_page = GroupPage(driver)
        group_page.click_on(self.LOGOUT)

