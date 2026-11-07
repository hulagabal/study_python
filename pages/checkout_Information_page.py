from playwright.sync_api import Page, expect

class CheckoutInformationPage:
    
    def __init__(self, page: Page):
        
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name =  page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.cancel_button = page.locator("#cancel")
        self.continue_button = page.locator("#continue")
        self.error = page.locator('[data-test="error"]')
        
    
    def verify_first_name_rquired_error(self):
        self.continue_button.click()
        expect(self.error).to_have_text("Error: First Name is required")
    
    def verify_last_name_required_error(self):
        self.first_name.fill("Mutturaj")
        self.continue_button.click()
        expect(self.error).to_have_text("Error: Last Name is required")
            
    def verify_postal_code_required_error(self):
        self.first_name.fill("Mutturaj")
        self.last_name.fill("Hulagabal")
        self.continue_button.click()
        expect(self.error).to_have_text("Error: Postal Code is required")
        
    def verify_cancel_return_to_cart(self):
        self.cancel_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
    
    def enter_valid_customer_info(self):
        self.first_name.fill("Mutturaj")
        self.last_name.fill("Hulagabal")
        self.postal_code.fill("586112")
        self.continue_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")