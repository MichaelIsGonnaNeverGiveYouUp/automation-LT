from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver.seleniumdriver import SeleniumDriver


class TopBannerPage:
    driver: webdriver = SeleniumDriver().webdriver

    # locators
    _cart_locator = "shopping_cart_container"

    # elements
    def get_cart_button(self):
        return self.driver.find_element(by=By.ID, value=self._cart_locator)

    # Actions
    def click_cart_button(self):
        self.get_cart_button().click()
