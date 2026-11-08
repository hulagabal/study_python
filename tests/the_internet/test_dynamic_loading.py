from playwright.sync_api import Page,  expect

def test_dynamic_loading_example_one(page:Page):
    
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    
    finish_text = page.locator("#finish")
    
    page.get_by_role("link", name= "Example 1: Element on page that is hidden").click()
    expect(finish_text).to_be_attached()
    
    page.get_by_role("button", name="Start").click()
    
    expect(finish_text).to_be_visible()
    expect(finish_text).to_have_text("Hello World!")

def test_dynamic_loading_example_two(page:Page):
    
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    
    finish_text = page.locator("#finish")
    
    page.get_by_role("link", name= "Example 2: Element rendered after the fact").click()
    expect(finish_text).not_to_be_attached()
    
    page.get_by_role("button", name="Start").click()
    
    expect(finish_text).to_be_visible()
    expect(finish_text).to_have_text("Hello World!")    