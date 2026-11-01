from playwright.sync_api import Page, expect
class InventoriesPage:
    def __init__(self, page: Page, product_name: str, product_price: str):
        self.page = page
        self.product_name_text = product_name
        self.product_price_text = product_price
        
        self.product = page.locator(".inventory_item").filter(has_text=self.product_name_text)
        self.product_name = self.product.locator(".inventory_item_name")
        self.product_price = self.product.locator(".inventory_item_price")
        self.product_add_cart_button = self.product.get_by_role("button", name="Add to cart")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
    
    
    def verify_product_details(self):
        expect(self.product_name).to_have_text(self.product_name_text)
        expect(self.product_price).to_have_text(self.product_price_text)

    def add_product_to_cart(self):
        expect(self.product_add_cart_button).to_be_visible()
        self.product_add_cart_button.click()
        expect(self.shopping_cart_link).to_have_text("1")
        
    def open_cart_page(self):    
        self.shopping_cart_link.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")