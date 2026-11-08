from decimal import Decimal
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_Information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage

from playwright.sync_api import Page

def test_checkout_overview(page:Page):
            
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
            
    inventory_page = InventoryPage(page)
    inventory_page.verify_product_details()
    inventory_page.add_product_to_cart()
    inventory_page.open_cart_page()
            
    cart_page = CartPage(page)
    cart_page.verify_cart_details()
    cart_page.click_checkout()
            
    checkout_information_page = CheckoutInformationPage(page)
    checkout_information_page.enter_valid_customer_info()
    
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.verify_overview_page_url()
    checkout_overview_page.verify_product_name("Sauce Labs Fleece Jacket")
    checkout_overview_page.verify_product_price("Sauce Labs Fleece Jacket","$49.99")
    checkout_overview_page.verify_quantity("Sauce Labs Fleece Jacket", "1")
    checkout_overview_page.verify_subtotal("$49.99")
    checkout_overview_page.verify_tax("$4.00")
    checkout_overview_page.verify_total(Decimal("53.99"))
    checkout_overview_page.click_finish()
    checkout_overview_page.verify_order_confirmation()
    checkout_overview_page.click_back_home()
    inventory_page.open_cart_page()
    cart_page.verify_cart_is_empty()