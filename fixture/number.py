from selenium.webdriver.common.by import By

from fixture.base_fixture import BaseHelper


class NumberHelper(BaseHelper):

    def type_firstname(self, newnum):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(newnum.first_name)
        driver.find_element(By.NAME, "middlename").clear()
        driver.find_element(By.NAME, "middlename").send_keys(newnum.middle_name)
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys(newnum.nickname)
        driver.find_element(By.NAME, "address2").clear()
        driver.find_element(By.NAME, "address2").send_keys(newnum.address2)

    def click_save(self):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()
        driver.find_element(By.LINK_TEXT, "home page").click()
    