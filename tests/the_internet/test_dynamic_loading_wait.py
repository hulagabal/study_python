from playwright.sync_api import Page, expect

def test_dynamic_loading_wait(page:Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.get_by_role("button", name="Start").click()
    
    expect(page.locator("#finish")).to_be_visible()