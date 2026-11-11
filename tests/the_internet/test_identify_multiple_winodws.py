from playwright.sync_api import Page, expect

def test_identify_multiple_windows(page:Page):
    page.goto("https://the-internet.herokuapp.com/windows")
    expect(page).to_have_title("The Internet")
    
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()
    
    new_window = next(
        page for page in page.context.pages
        if "new" in page.url
    )
    
    expect(new_window).to_have_title("New Window")
    
    expect(new_window).to_have_url("https://the-internet.herokuapp.com/windows/new")
    expect(new_window.get_by_role("heading", name= "New Window")).to_be_visible()