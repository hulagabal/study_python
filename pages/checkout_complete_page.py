from playwright.sync_api import Page, expect

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = self.page.locator(".complete-header")
        self.back_home_button = self.page.get_by_role("button", name="Back Home")
        
    def verify_order_confirmation(self):
        expect(self.header).to_have_text("Thank you for your order!")
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
            
    def click_back_home(self):
        self.back_home_button.click()    
    