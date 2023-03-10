from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver.seleniumdriver import SeleniumDriver


class CheckoutYourInfoPage:

    driver: webdriver = SeleniumDriver().webdriver

    # locators
    _first_name_locator = "first-name"
    _last_name_locator = "last-name"
    _postal_code_locator = "postal-code"
    _continue_locator = "continue"
    _cancel_locator = "cancel"

    # elements
    def get_first_name(self):
        return self.driver.find_element(by=By.ID, value=self._first_name_locator)

    def get_last_name(self):
        return self.driver.find_element(by=By.ID, value=self._last_name_locator)

    def get_postal_code(self):
        return self.driver.find_element(by=By.ID, value=self._postal_code_locator)

    def get_continue(self):
        return self.driver.find_element(by=By.ID, value=self._continue_locator)

    def get_cancel(self):
        return self.driver.find_element(by=By.ID, value=self._cancel_locator)

    # Actions
    def enter_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)

    def enter_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.get_postal_code().clear()
        self.get_postal_code().send_keys(postal_code)

    def fill_out_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        self.get_continue().click()

    def click_cancel(self):
        self.get_cancel().click()
