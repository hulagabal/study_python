from playwright.sync_api import Page, expect

class ProductCartPage:
    def __init__(self, page: Page, product_name: str, product_price: str):
        
        self.page = page
        self.product_name_text = product_name
        self.product_price_text = product_price

        self.cart_item = page.locator(".cart_item").filter(has_text=product_name)
        self.cart_item_name = self.cart_item.locator(".inventory_item_name")
        self.cart_item_price = self.cart_item.locator(".inventory_item_price")
        self.cart_quantity_count = self.cart_item.locator(".cart_quantity")
        self.remove_button = self.cart_item.get_by_role("button", name="Remove")
        self.cart_item_count = page.locator(".cart_item")
    
    
    def verify_cart_details(self):
        
        expect(self.cart_item_name).to_have_text(self.product_name_text)
        expect(self.cart_quantity_count).to_have_text("1")
        expect(self.cart_item_price).to_have_text(self.product_price_text)
        expect(self.remove_button).to_be_enabled()
    
    def remove_item_from_cart(self):

        self.remove_button.click()
    
    def verify_cart_is_empty(self):
        
        expect(self.cart_item_count).to_have_count(0)    