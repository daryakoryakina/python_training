from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    # подается драйвер. на каждой странице должна быть. Точнее нет, ведь для этого BasePage
    def __init__(self, driver):
        self.driver = driver

    # библиотека ec для получения элемента с локатором, библиотека wait и сам метод
    # ждет, пока элемент появится в течении 10 секунд. Нет элемента, падает тест
    def get_element(self, locator):
        expected_conditions = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_conditions, message="Unable to locate element")

    # в функцию подаются разные элементы с локаторами, заданными в тесте, элемент получается и подается в
    # verify page для проверки, есть ли элемент на странице
    def on_this_page(self, *args):
        for locator in args:
            self.get_element(locator)

    # кликнуть на элемент с локатором
    def click_on(self, locator):
        self.get_element(locator).click()

    # для элемента с вводом - очистить поле, ввести текст
    def type_in(self, locator, text):
        self.get_element(locator).send_keys(text)

    def clear_input(self, locator):
        self.get_element(locator).clear()