from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver.seleniumdriver import SeleniumDriver


class CheckoutOverviewPage:

    driver: webdriver = SeleniumDriver().webdriver

    # locators
    _checkout_overview_locator = "checkout_summary_container"
    _finish_locator = "finish"
    _cancel_locator = "cancel"
    _item_name_locator = "inventory_item_name"

    # elements
    def get_checkout_overview(self):
        return self.driver.find_element(by=By.ID, value=self._checkout_overview_locator)

    def get_finish(self):
        return self.driver.find_element(by=By.ID, value=self._finish_locator)

    def get_cancel(self):
        return self.driver.find_element(by=By.ID, value=self._cancel_locator)

    def get_cart_item_by_name(self, item_name):
        return self.driver.find_element(by=By.XPATH, value=f"//div[contains(text(), '{item_name}')]")

    # Actions
    def click_finish(self):
        self.get_finish().click()

    def click_cancel(self):
        self.get_cancel().click()
