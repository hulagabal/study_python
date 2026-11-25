from playwright.sync_api import Page

def test_pop_window(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    print("CURRENT URL:", page.url)
    print("PAGE TITLE:", page.title())
    print("PAGE CONTENT:", page.locator("body").inner_text()[:1500])
        
    with page.expect_popup() as pop_window_info:
        page.get_by_role("button", name="Popup Windows").click()
        
    new_page = pop_window_info.value
    new_page.wait_for_load_state()
        
    print(new_page.title())
    print(new_page.url)

def test_multiple_pops(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html") 
        
    popups =[]
    page.on("popup", lambda popup: popups.append(popup))    
    page.get_by_role("button", name= "Popup Windows").click()
        
    print(len(popups))
        
    for index, popup in enumerate(popups, start=1):        
        print(popup.title())
        popup.close()