from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.parametrize("username, password, locator, expected_text",  
                         [("admin", "admin", ".example p", "Congratulations! You must have the proper credentials."),
                          ("admin", "wrong", "body", "Not authorized")])
def test_basic_auth(username, password, locator, expected_text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(http_credentials={
            "username": username,
            "password": password
        })
        
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/basic_auth")
            
        expect(page.locator(locator)).to_have_text(expected_text)