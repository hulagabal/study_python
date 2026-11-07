from playwright.sync_api import Page, expect
class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product = page.locator(".inventory_item").filter(has_text="Sauce Labs Fleece Jacket")
        self.product_name = self.product.locator(".inventory_item_name")
        self.product_price = self.product.locator(".inventory_item_price")
        self.product_add_cart_button = self.product.get_by_role("button", name="Add to cart")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
    
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
    
    
    def add_products_to_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_add_to_cart = product.get_by_role("button", name="Add to cart")
        product_add_to_cart.click()
        
    def remove_product_from_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_remove_from_cart = product.get_by_role("button", name="Remove")
        product_remove_from_cart.click()
    
    def verify_filter_az(self):
        
        original_products_names = self.page.locator(".inventory_item_name").all_inner_texts()
        expected_product_names = sorted(original_products_names)
        
        self.page.locator(".product_sort_container").select_option("az")
        expect(self.page.locator(".inventory_item_name")).to_have_text(expected_product_names)
    
    def verify_filter_za(self):
        
        original_product_names = self.page.locator(".inventory_item_name").all_inner_texts()
        expected_product_name = sorted(original_product_names, reverse=True) 
        
        self.page.locator(".product_sort_container").select_option("za")
        expect(self.page.locator(".inventory_item_name")).to_have_text(expected_product_name)
        
    def verify_price_filter_low_to_high(self):
        
        original_price_locator = self.page.locator(".inventory_item_price").all_inner_texts()
        float_prices = self.convert_price(original_price_locator)
        expected_prices = sorted(float_prices)
        formatted_prices = [f"${expected_price:.2f}" for expected_price in expected_prices]
        
        self.page.locator(".product_sort_container").select_option("lohi")
        expect(self.page.locator(".inventory_item_price")).to_have_text(formatted_prices)
    
    def verify_price_filter_high_to_low(self):
        
        original_price_locator = self.page.locator(".inventory_item_price").all_inner_texts()
        float_prices = self.convert_price(original_price_locator)
        expected_prices = sorted(float_prices, reverse=True)
        formatted_prices = [f"${expected_price:.2f}" for expected_price in expected_prices]
        
        self.page.locator(".product_sort_container").select_option("hilo")
        expect(self.page.locator(".inventory_item_price")).to_have_text(formatted_prices)
        
    def convert_price(self, product_prices: list[str]) -> list[float]:
        prices =[]
        for product_price in product_prices:
            float_price = float(product_price.replace("$", ""))
            prices.append(float_price)
        return prices
    
    def verify_default_sorting_option(self):
        
        expect(self.sort_dropdown).to_have_value("az")
    
    def verify_all_dropdown_option(self):
        expected_labels = ['Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)']
        actual_labels = self.sort_dropdown.locator("option").all_inner_texts()
        
        assert actual_labels == expected_labels
        
        expected_values = ["az", "za", "lohi", "hilo"]
        actual_values = self.sort_dropdown.locator("option").evaluate_all("(options) => options.map(option => option.value)")
        
        assert actual_values == expected_values