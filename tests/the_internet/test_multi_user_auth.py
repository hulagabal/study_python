from playwright.sync_api import Browser, expect


def test_multi_user_auth(browser: Browser):
    try:
        standard_context = browser.new_context()
        problem_context =  browser.new_context()
        
        standard_page =  standard_context.new_page()
        problem_page = problem_context.new_page()
        
        standard_page.goto("https://www.saucedemo.com/")
        problem_page.goto("https://www.saucedemo.com/")
        
        standard_page.locator("#user-name").fill("standard_user")
        problem_page.locator("#user-name").fill("problem_user")
        
        standard_page.locator("#password").fill("secret_sauce")
        problem_page.locator("#password").fill("secret_sauce")
        
        std_login_button = standard_page.locator("#login-button")
        prb_login_button = problem_page.locator("#login-button")
        
        std_login_button.click()
        prb_login_button.click()
        
        expect(standard_page.locator(".app_logo")).to_have_text("Swag Labs")
        expect(problem_page.locator(".app_logo")).to_have_text("Swag Labs")
        
        standard_page.locator("#react-burger-menu-btn").click()
        
        standard_page.locator("#logout_sidebar_link").click()
        
        expect(std_login_button).to_be_visible()
        expect(problem_page.locator(".inventory_list")).to_be_visible()
    
    finally:
        standard_context.close()
        problem_context.close()