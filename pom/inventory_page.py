from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver.seleniumdriver import SeleniumDriver


class InventoryPage:

    driver: webdriver = SeleniumDriver().webdriver

    # locators
    _cart_locator = "shopping_cart_container"
    _checkout_locator = "checkout"
    _inventory_item = "inventory_item"

    # elements
    def get_cart(self):
        return self.driver.find_element(by=By.ID, value=self._cart_locator)

    def get_checkout(self):
        return self.driver.find_element(by=By.ID, value=self._checkout_locator)

    def get_inventory_items(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value=self._inventory_item)

    def get_inventory_item_by_name(self, item_name):
        return self.driver.find_element(by=By.XPATH, value=f"//div[contains(text(), '{item_name}')]")

    # Actions
    def add_item_to_cart(self, cart_item_id):
        self.driver.find_element(value=cart_item_id, by=By.ID).click()

    def click_cart(self):
        self.get_cart().click()
