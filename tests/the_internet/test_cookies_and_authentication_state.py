from playwright.sync_api import Browser, expect

def test_cookies_and_authentication_state(browser: Browser):
    try:
        
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://www.saucedemo.com/")
        
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        
        cookies = context.cookies()
        assert len(cookies) > 0
        
        context.storage_state(path="auth.json")
        new_context = browser.new_context(storage_state="auth.json")
        new_page = new_context.new_page()
        new_page.goto("https://www.saucedemo.com/inventory.html")
        
        expect(new_page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(new_page.locator(".app_logo")).to_have_text("Swag Labs")
        expect(new_page.locator("#item_4_title_link")).to_have_text("Sauce Labs Backpack")
        
    
    finally:
        context.close()
        new_context.close()
            