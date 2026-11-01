from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_specific_product(page: Page):
    
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    inventory_page = InventoryPage(page)        
    inventory_page.verify_product_details()
    inventory_page.add_product_to_cart()
    inventory_page.open_cart_page()

    cart_page = CartPage(page)
    cart_page.verify_cart_details()
    cart_page.remove_item_from_cart()
    cart_page.verify_cart_is_empty()   