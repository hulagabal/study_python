from playwright.sync_api import Browser, expect

def test_session_isolation(browser: Browser):
    try:
        context1 = browser.new_context()
        context2 = browser.new_context()
        
        page1 = context1.new_page()
        page2 = context2.new_page()
        
        page1.goto("https://the-internet.herokuapp.com/login")
        page1.locator("#username").fill("tomsmith")
        page1.locator("#password").fill("SuperSecretPassword!")
        page1.locator("button[type='submit']").click()
        
        expect(page1.get_by_role("link", name=" Logout")).to_be_visible()
        
        page2.goto("https://the-internet.herokuapp.com/secure")
        expect(page2.locator("#flash")).to_contain_text("You must login to view the secure area!")
    finally:
        context1.close()
        context2.close()