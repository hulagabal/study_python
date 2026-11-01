from playwright.sync_api import Page, expect
class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product = page.locator(".inventory_item").filter(has_text="Sauce Labs Fleece Jacket")
        self.product_name = self.product.locator(".inventory_item_name")
        self.product_price = self.product.locator(".inventory_item_price")
        self.product_add_cart_button = self.product.get_by_role("button", name="Add to cart")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
    
    def verify_product_details(self):
        expect(self.product_name).to_have_text("Sauce Labs Fleece Jacket")
        expect(self.product_price).to_have_text("$49.99")
        
    def add_product_to_cart(self):    
        expect(self.product_add_cart_button).to_be_visible()
        self.product_add_cart_button.click()
        expect(self.shopping_cart_link).to_have_text("1")
        
    def open_cart_page(self):    
        self.shopping_cart_link.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
        
        
    