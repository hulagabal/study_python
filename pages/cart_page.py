from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator(".cart_item").filter(has_text="Sauce Labs Fleece Jacket")
        self.cart_item_name = self.cart_item.locator(".inventory_item_name")
        self.cart_item_price = self.cart_item.locator(".inventory_item_price")
        self.cart_quantity_count = self.cart_item.locator(".cart_quantity")
        self.remove_button = self.cart_item.get_by_role("button", name="Remove")
        self.cart_item_count = page.locator(".cart_item")
    
    
    def verify_cart_details(self):
        
        expect(self.cart_item_name).to_have_text("Sauce Labs Fleece Jacket")
        expect(self.cart_quantity_count).to_have_text("1")
        expect(self.cart_item_price).to_have_text("$49.99")
        expect(self.remove_button).to_be_visible()  
    
    def remove_item_from_cart(self):

        self.remove_button.click()
    
    def verify_cart_is_empty(self):
        
        expect(self.cart_item_count).to_have_count(0)    