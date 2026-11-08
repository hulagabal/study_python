from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from pages.login_page import LoginPage

def test_add_remove_multiple_products(page:Page):
    login_page =LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page =InventoryPage(page)
    cart_page = CartPage(page)
    
    inventory_page.add_products_to_cart("Sauce Labs Backpack")
    inventory_page.add_products_to_cart("Sauce Labs Bike Light")
    inventory_page.add_products_to_cart("Sauce Labs Bolt T-Shirt")
    cart_page.verify_cart_count("3")
    
    inventory_page.remove_product_from_cart("Sauce Labs Bolt T-Shirt")
    cart_page.verify_cart_count("2")
    
    cart_page.click_shopping_cart()
    cart_page.verify_cart_product("Sauce Labs Backpack")
    cart_page.verify_cart_product("Sauce Labs Bike Light")
    
    cart_page.remove_product_from_cart("Sauce Labs Bike Light")
    cart_page.verify_cart_count("1")
    
    cart_page.verify_cart_product("Sauce Labs Backpack")
    cart_page.very_product_not_in_cart("Sauce Labs Bike Light")