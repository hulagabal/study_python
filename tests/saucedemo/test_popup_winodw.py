from playwright.sync_api import Page

def test_pop_window(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
    with page.expect_popup() as pop_window_info:
        page.get_by_role("button", name="Popup Windows").click()
        
    new_page = pop_window_info.value
        
    print(new_page.title())
    print(new_page.url)

def test_multiple_pops(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html") 
        
    popups =[]
    page.on("popup", lambda popup: popups.append(popup))    
    page.get_by_role("button", name= "Popup Windows").click()
        
    print(len(popups))
        
    for popup in enumerate(popups, start=1):        
        print(popup.title())
        popup.close()