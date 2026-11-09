from playwright.sync_api import Page, expect

def test_tabs(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")
    
    expect(page.get_by_role("heading", name="Opening a new window")).to_have_text("Opening a new window")
    
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()
    
    popup = popup_info.value
    
    expect(popup).to_have_title("New Window")
    expect(popup.get_by_role("heading", name="New Window")).to_have_text("New Window")