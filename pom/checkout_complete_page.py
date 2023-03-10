from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver.seleniumdriver import SeleniumDriver


class CheckoutCompletePage:

    driver: webdriver = SeleniumDriver().webdriver

    # locators
    _back_to_homepage_locator = "back-to-products"
    _header_container_locator = "header_container"
    _checkout_complete_text = "Checkout: Complete!"

    # elements

    def get_back_to_homepage_button(self):
        return self.driver.find_element(by=By.ID, value=self._back_to_homepage_locator)

    def get_header_container(self):
        return self.driver.\
            find_element(by=By.ID, value=self._header_container_locator).find_element(by=By.CLASS_NAME, value="title")

    # Actions
    def click_back_to_homepage(self):
        self.get_back_to_homepage_button().click()

    def verify_checkout_complete(self):
        return self.get_header_container().text == self._checkout_complete_text
