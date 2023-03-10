from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver.seleniumdriver import SeleniumDriver


class LoginPage:

    driver: webdriver = SeleniumDriver().webdriver

    _error_message = "Epic sadface: Username and password do not match any user in this service"

    # locators
    _error_message_locator = f"//*[contains(text(),'{_error_message}')]"
    _username_field_locator = "user-name"
    _password_field_locator = "password"
    _login_button_locator = "login-button"

    # elements
    def get_error_message(self):
        return self.driver.find_element(by=By.XPATH, value=self._error_message_locator)

    def get_username_field(self):
        return self.driver.find_element(by=By.ID, value=self._username_field_locator)

    def get_password_field(self):
        return self.driver.find_element(by=By.ID, value=self._password_field_locator)

    def get_login_button(self):
        return self.driver.find_element(by=By.ID, value=self._login_button_locator)

    # actions
    def enter_username(self, username):
        self.get_username_field().clear()
        self.get_username_field().send_keys(username)

    def enter_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def verify_login_failed(self):
        return self.get_error_message().is_displayed()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
