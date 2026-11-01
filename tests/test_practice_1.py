import os
from pypdf import PdfReader
from playwright.sync_api import sync_playwright, expect

from utils.pdf_helper import validate_pdf

def test_saucedemo_login(tmp_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        try:
            
            page=browser.new_page()
            page.goto("https://www.saucedemo.com/")
            page.get_by_placeholder("Username").fill("standard_user")
            page.get_by_placeholder("Password").fill("secret_sauce")
            page.get_by_role("button", name="Login").click()
            
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
            
            page.locator(".product_sort_container").select_option("hilo")
            
            item_count = page.locator(".inventory_item").count()
            print(f"Total number of items: {item_count}")
            
            expected_titles = ['Sauce Labs Fleece Jacket',
                               'Sauce Labs Backpack',
                               'Sauce Labs Bolt T-Shirt',
                               'Test.allTheThings() T-Shirt (Red)',
                               'Sauce Labs Bike Light',
                               'Sauce Labs Onesie']
            expected_prices = ['$49.99', '$29.99', '$15.99',
                               '$15.99', '$9.99', '$7.99']
            
            expect(page.locator(".inventory_item_name")).to_have_text(expected_titles)
            expect(page.locator(".inventory_item_price")).to_have_text(expected_prices)             
            
            first_item = page.locator(".inventory_item").first
            expect(first_item.locator(".inventory_item_name")).to_have_text("Sauce Labs Fleece Jacket")
            expect(first_item.locator(".inventory_item_price")).to_have_text("$49.99")
            
            first_add_cart_button=first_item.get_by_role("button", name="Add to cart")
            first_add_cart_button.click()
            
            expect(first_item.get_by_role("button", name="Remove")).to_be_visible()
            shopping_cart_link = page.locator(".shopping_cart_link")
            expect(shopping_cart_link).to_have_text("1")
            shopping_cart_link.click()
            
            expect(page).to_have_url("https://www.saucedemo.com/cart.html")
            
            inventory_name = page.locator(".inventory_item_name")
            inventory_price =page.locator(".inventory_item_price")
            
            expect(inventory_name).to_have_text("Sauce Labs Fleece Jacket")
            expect(inventory_price).to_have_text("$49.99")
            expect(page.get_by_role("button", name="Continue Shopping")).to_be_visible()
            
            page.get_by_role("button", name="Checkout").click()
            page.get_by_placeholder("First Name").fill("Mutturaj")
            page.get_by_placeholder("Last Name").fill("Hulagabal")
            page.get_by_placeholder("Zip/Postal Code").fill("586112")
            page.get_by_role("button", name="continue").click()
            
            expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
            
            expect(inventory_name).to_have_text("Sauce Labs Fleece Jacket")
            expect(inventory_price).to_have_text("$49.99")
            
            expect(page.locator('[data-test="payment-info-value"]')).to_have_text("SauceCard #31337")
            expect(page.locator('[data-test="shipping-info-value"]')).to_have_text("Free Pony Express Delivery!")
            expect(page.locator('[data-test="subtotal-label"]')).to_have_text("Item total: $49.99")
            expect(page.locator('[data-test="tax-label"]')).to_have_text("Tax: $4.00")
            expect(page.locator('[data-test="total-label"]')).to_have_text("Total: $53.99")
            
            cancel_button = page.get_by_role("button", name= "cancel")
            expect(cancel_button).to_be_visible()
            
            finish_button= page.get_by_role("button", name= "Finish")
            expect(finish_button).to_be_visible()
            finish_button.click()
            
            expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
            
            generate_pdf_button = page.get_by_role("button", name= "Generate PDF order")
            expect(generate_pdf_button).to_be_enabled()
            
            with page.expect_download() as download_info:
                generate_pdf_button.click()
            
            download = download_info.value
            
            target_path = tmp_path / 'my_order.pdf'
            download.save_as(target_path)
                        
            assert os.path.exists(target_path) and os.path.getsize(target_path) > 0 , f'file missing or empty at {target_path}'
            
            expected_keywords = ["$53.99", "$49.99", "$4.00", "Mutturaj Hulagabal", "Sauce Labs Fleece Jacket"]
            
            validate_pdf(target_path, expected_keywords)
            
            page.get_by_role("button", name="Open Menu").click()
            logout_link = page.get_by_text("Logout")
            expect(logout_link).to_be_visible()
            logout_link.click()
            
            expect(page).to_have_url("https://www.saucedemo.com/")
            
        finally:    
            browser.close()