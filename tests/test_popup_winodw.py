from playwright.sync_api import sync_playwright

def test_pop_window():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page= browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        with page.expect_popup() as pop_window_info:
            page.get_by_role("button", name="Popup Windows").click()
        
        new_page = pop_window_info.value
        
        print(new_page.title())
        print(new_page.url)
        
        new_page.close()
        browser.close()


def test_multiple_pops():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        
        page = browser.new_page()
        
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html") 
        
        popups =[]
        
        page.on("popup", lambda popup: popups.append(popup))
        
        
        page.get_by_role("button", name= "Popup Windows").click()
        
        print(len(popups))
        
        for index, popup in enumerate(popups, start=1):
            
            print(popup.title())
            
            popup.close()          
            
        