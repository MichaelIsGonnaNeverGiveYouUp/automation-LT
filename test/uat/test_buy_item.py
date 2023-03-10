import time

import pytest

from pom.cart_page import CartPage
from pom.checkout_complete_page import CheckoutCompletePage
from pom.checkout_overview_page import CheckoutOverviewPage
from pom.checkout_your_info_page import CheckoutYourInfoPage
from pom.inventory_page import InventoryPage
from pom.login_page import LoginPage
from pom.top_banner_page import TopBannerPage
from util.util import password
from webdriver.seleniumdriver import SeleniumDriver

driver = SeleniumDriver().get_webdriver_instance()


@pytest.fixture(scope="session")
def fixture_login():
    login_page = LoginPage()
    login_page.login("standard_user", password)
    yield
    driver.quit()


def get_id_for_item(item_name):
    return f'add-to-cart-{item_name.replace(" ", "-").lower()}'


def get_items_to_test():
    return ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket"]


# We have 2 options: Parametrize with a fixed list, or get the list with find_elements
@pytest.mark.parametrize("item_name", get_items_to_test())
def test_buy_item(item_name, fixture_login):

    # Create the page objects
    inventory_page = InventoryPage()
    cart_page = CartPage()
    top_banner_page = TopBannerPage()
    checkout_overview_page = CheckoutOverviewPage()
    checkout_your_info_page = CheckoutYourInfoPage()
    checkout_complete_page = CheckoutCompletePage()

    # Getting the item name from the page before moving to the next screen
    item_name_on_page = inventory_page.get_inventory_item_by_name(item_name).text.strip()
    # ID's have spaces replaced with dashes and are all lowercase
    item_id = get_id_for_item(item_name)
    inventory_page.add_item_to_cart(item_id)
    top_banner_page.click_cart_button()
    # Verify that the item is in the cart
    assert cart_page.get_cart_item_by_name(item_name_on_page).text == item_name

    cart_page.click_checkout()
    # Fill out the checkout form
    checkout_your_info_page.fill_out_form("John", "Doe", "12345")
    checkout_your_info_page.click_continue()

    # validate that the item is in the checkout overview
    assert checkout_overview_page.get_cart_item_by_name(item_name_on_page).text == item_name

    # Click finish
    checkout_overview_page.click_finish()

    # Validate checkout has been completed
    assert checkout_complete_page.verify_checkout_complete()

    checkout_complete_page.click_back_to_homepage()




