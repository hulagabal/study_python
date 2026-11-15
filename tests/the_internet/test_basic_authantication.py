from playwright.sync_api import Browser, expect
import pytest

@pytest.mark.parametrize("username, password, locator, expected_text",  
                         [("admin", "admin", ".example p", "Congratulations! You must have the proper credentials."),
                          ("admin", "wrong", "body", "Not authorized")])
def test_basic_auth(browser: Browser,username, password, locator, expected_text):
    
        context = browser.new_context(http_credentials={
            "username": username,
            "password": password
        })
        
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/basic_auth")
            
        expect(page.locator(locator)).to_have_text(expected_text)
        
        
# • Why this is necessary: HTTP Basic Auth triggers a native browser-level pop-up, which standard HTML locators cannot interact with.
# • How Playwright solves it: By passing http_credentials into browser.new_context(), you create an isolated browser session (similar to an Incognito window) that automatically 
#   injects the username and password into the HTTP request headers whenever the server asks for authentication.
# • context.new_page() then opens a new tab inside that authenticated session.