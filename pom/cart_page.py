from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver.seleniumdriver import SeleniumDriver


class CartPage:
    driver: webdriver = SeleniumDriver().webdriver

    # locators
    items_in_cart = "cart_item"
    item_name = "inventory_item_name"
    item_price = "inventory_item_price"
    item_quantity = "cart_quantity"
    item_total = "inventory_item_price"
    checkout_button = "checkout"
    continue_shopping_button = "continue-shopping"
    remove_button = "remove-sauce-labs-backpack"

    # elements
    def get_items_in_cart(self):
        return self.driver.find_elements(by=By.ID, value=self.items_in_cart)

    def get_item_name(self, element):
        return element.find_element(by=By.CLASS_NAME, value=self.item_name)

    def get_item_price(self, element):
        return element.find_element(by=By.CLASS_NAME, value=self.item_price)

    def get_item_remove_button(self, element):
        return element.find_element(by=By.ID, value=self.remove_button)

    def get_item_quantity(self, element):
        return element.find_element(by=By.CLASS_NAME, value=self.item_quantity)

    def get_item_total(self, element):
        return element.find_element(by=By.CLASS_NAME, value=self.item_total)

    def click_continue_shopping(self):
        return self.driver.find_element(by=By.ID, value=self.continue_shopping_button)

    def click_checkout(self):
        return self.driver.find_element(by=By.ID, value=self.checkout_button).click()

    def get_cart_item_by_name(self, item_name):
        return self.driver.find_element(by=By.XPATH, value=f"//div[contains(text(), '{item_name}')]")


