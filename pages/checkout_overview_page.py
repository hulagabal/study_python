from playwright.sync_api import Page ,expect

class CheckoutOverviewPage:
    
    def __init__(self, page: Page):
        
        self.page = page
        self.item_price = self.page.locator(".inventory_item_price")
        self.quantity = self.page.locator(".cart_quantity")
        self.sub_total = self.page.locator(".summary_subtotal_label")
        self.tax = self.page.locator(".summary_tax_label")
        self.total = self.page.locator(".summary_total_label")
        
    def verify_overview_page_url(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    
    def verify_product_name(self, expected_name):
        
        self.item_name= self.filtered_item(expected_name).locator(".inventory_item_name")
        expect(self.item_name).to_contain_text(expected_name)
    
    def verify_product_price(self, expected_name, expected_price):
        self.item_price = self.filtered_item(expected_name).locator(".inventory_item_price")
        
        expect(self.item_price).to_contain_text(expected_price)
        
    def verify_quantity(self, expected_name, expected_quantity):
        self.item_quantity = self.filtered_item(expected_name).locator(".cart_quantity")
        expect(self.item_quantity).to_have_text(expected_quantity)
    
    
    def verify_subtotal(self, expected_subtotal):
        expect(self.sub_total).to_contain_text(expected_subtotal)
    
    def verify_tax(self, expected_tax):
        expect(self.tax).to_contain_text(expected_tax)
    
    def verify_total(self, expected_total):
        
        print(self.sub_total.inner_text())
        print(self.tax.inner_text())
        print(self.total.inner_text())
        
    def filtered_item(self, item_name):
        return self.page.locator(".cart_item").filter(has_text=item_name)    
            
            
    