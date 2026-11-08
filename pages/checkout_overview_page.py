from playwright.sync_api import Page ,expect
from decimal import Decimal

class CheckoutOverviewPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.sub_total = self.page.locator(".summary_subtotal_label")
        self.tax = self.page.locator(".summary_tax_label")
        self.total = self.page.locator(".summary_total_label")
        self.finish_button = self.page.locator("#finish")
        self.back_home_button = self.page.get_by_role("button", name="Back Home")
        
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
    
    def verify_total(self, expected_total: Decimal):
        subtotal_amount = self.convert_price_to_decimal(self.sub_total)
        tax_amount = self.convert_price_to_decimal(self.tax)
        displayed_amount = self.convert_price_to_decimal(self.total)
        
        assert subtotal_amount + tax_amount == expected_total == displayed_amount
        
    def click_finish(self):
        self.finish_button.click()
        
    def verify_order_confirmation(self):
        expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
        
    def click_back_home(self):
        self.back_home_button.click()    
        
    def filtered_item(self, item_name):
        return self.page.locator(".cart_item").filter(has_text=item_name)
    
    def convert_price_to_decimal(self, locator):
        price_data = locator.inner_text().split("$")
        price_string = price_data[1].strip()
        price_number = Decimal(price_string)
        return price_number