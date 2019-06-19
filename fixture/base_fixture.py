from selenium.webdriver.common.by import By


class BaseHelper:

    def __init__(self, app):
        self.app = app

    # базовый метод открытия нужной страницы и валидации страницы.
    def open(self, base):
        driver = self.app.driver
        if not (driver.current_url.endswith(base.endswith) and len(driver.find_elements(By.NAME, base.name)) > 0):
            driver.find_element(By.LINK_TEXT, base.page).click()

    def assert_page_without_uri(self, base):
        driver = self.app.driver
        if not (len(driver.find_elements(By.NAME, base.name)) > 0):
            driver.find_element(By.LINK_TEXT, base.page).click()

