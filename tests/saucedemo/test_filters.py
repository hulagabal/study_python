from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def ttest_dynamic_product_sorting(page:Page):
    login_page =LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    
    inventory_page.verify_price_filter_low_to_high()
    inventory_page.verify_filter_za()
    inventory_page.verify_price_filter_high_to_low()
    inventory_page.verify_filter_az()
    
def test_dropdown_validation(page: Page):
    login_page =LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    
    inventory_page.verify_default_sorting_option()
    
    inventory_page.verify_all_dropdown_option()
        