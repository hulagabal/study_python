from playwright.sync_api import sync_playwright

import re

def test_practice_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        
        page.get_by_role("button", name="Primary Action").click()
        page.get_by_role("button", name="Toggle Button").click()
        print(page.get_by_role("button", name="Div with button role").inner_text())
        page.get_by_role("textbox", name="Username:").fill("muttu")
        page.get_by_role("checkbox", name=" Accept terms").check()
        
        page.get_by_role("menuitem", name="Home").click()
        print("Home clicked")
        page.get_by_role("menuitem", name="Products").click()
        page.get_by_role("menuitem", name="Contact").click()
        
        alert=page.get_by_text("This is an important alert message!")
        alert_text = alert.inner_text()
        print(f"Alert message:  {alert_text}")
        assert alert.is_visible()
        
        
        #Get By label
        page.get_by_label(text="Email Address:").fill("hulagabal@gmail.com")
        page.get_by_label(text="Password:").fill("Muttu")
        page.get_by_label(text="Your Age:").fill("20")
        page.get_by_label(text="Express").check()
        
        #Get By text
        print(page.get_by_text(text=" important text").inner_text())
        print(page.get_by_text(re.compile("colored text", re.IGNORECASE)).inner_text())
        print(page.get_by_text(re.compile("^This paragraph")).inner_text())