from selenium.webdriver.common.by import By


class BaseHelper:

    def __init__(self, app):
        self.app = app

# базовый метод открытия нужной страницы и валидации страницы.
    def open(self, page, endswith, name):
        driver = self.app.driver
        if not (driver.current_url.endswith(endswith) and len(driver.find_elements(By.NAME, name)) > 0):
            driver.find_element(By.LINK_TEXT, page).click()

# базовый метод подсчета чекбоксов на открытой странице. Параметры endswith, name передаются для метода open, который
    # открывает и валидирует страницу, на которой считаются чекбоксы
    def count(self, page, endswith, name):
        driver = self.app.driver
        self.open(page, endswith, name)
        return len(driver.find_elements(By.NAME, "selected[]"))








