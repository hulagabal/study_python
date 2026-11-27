from playwright.sync_api import Page, expect

def test_login_with_api_created_account(page: Page, automation_exercise_account):
    account_data = automation_exercise_account
    
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name="Signup / Login").click()
    
    login_section = page.get_by_role("heading", name="Login to your account")
    
    expect(login_section).to_be_visible()
    
    email_input = page.locator('[data-qa="login-email"]')
    expect(email_input).to_be_visible()
    email_input.fill(account_data["email"])
    
    password_input = page.locator('[data-qa="login-password"]')
    expect(password_input).to_be_visible()
    password_input.fill(account_data["password"])
    
    login_btn = page.locator('[data-qa="login-button"]')
    expect(login_btn).to_be_visible()
    login_btn.click()
    
    logged_in_banner = page.locator("li").filter(has_text=f"Logged in as {account_data['name']}")
    expect(logged_in_banner).to_be_visible()
    
    product_banner = page.get_by_role("link", name=" Products")
    expect(product_banner).to_be_visible()
    product_banner.click()
    
    expect(page).to_have_url("https://automationexercise.com/products")
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()
    
    single_product = page.locator(".single-products").first
    expect(single_product).to_be_visible()
    
    blue_top_card = page.locator(".single-products").filter(has_text="Blue Top")
    add_to_cart_btn = blue_top_card.locator(".productinfo .add-to-cart")
    expect(add_to_cart_btn).to_be_visible()
    add_to_cart_btn.click()
    
    expect(page.locator("#cartModal")).to_be_visible()
    page.get_by_role("button", name="Continue Shopping").click()
    cart_link = page.get_by_role("link", name= " Cart")
    expect(cart_link).to_be_visible()
    cart_link.click()
    
    blue_top_row = page.locator("#product-1")
    expect(blue_top_row).to_be_visible()

    expect(blue_top_row.locator(".cart_description h4 a")).to_have_text("Blue Top")
    expect(blue_top_row.locator(".cart_quantity button")).to_have_text("1")
