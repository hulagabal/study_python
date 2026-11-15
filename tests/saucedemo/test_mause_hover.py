from playwright.sync_api import Page, expect

def test_mause_hover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
        
    page.wait_for_load_state("load")
        
    mobile_option = page.locator(".dropdown-content").get_by_text("Mobiles")
    laptop_option = page.locator(".dropdown-content").get_by_text("Laptops")
        
    expect(mobile_option).not_to_be_visible()
    expect(laptop_option).not_to_be_visible()
        
    page.get_by_role("button", name="Point Me").hover()
        
    expect(mobile_option).to_be_visible()
    expect(laptop_option).to_be_visible()


def test_slider(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_load_state("load")
        
    slider_handle = page.locator(".ui-slider-handle").first
    slider_handle.focus()
        
    for _ in range(5):
        page.keyboard.press("ArrowRight")
        
    expect(page.locator("#amount")).to_be_visible()
    print(page.locator("#amount").inner_text())    