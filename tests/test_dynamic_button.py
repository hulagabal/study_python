from playwright.sync_api import sync_playwright, expect

def test_dynamic_button():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False, slow_mo=1000)
        page= browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        start, stop = page.get_by_role("button", name="START"), page.get_by_role("button", name="STOP")
         
        expect(start).to_be_visible()
        expect(stop).to_be_hidden()
        
        start.click()
        expect(start).to_be_hidden()
        expect(stop).to_be_visible()
        
        stop.click()
        expect(start).to_be_visible()
        
def test_new_tab():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        
        with page.expect_popup() as page_info:
            page.get_by_role("button", name="New Tab").click()
        
        
        new_page = page_info.value
        
        new_page.wait_for_load_state()
        
        print(f"New page Title is {new_page.title()}" )
        
        expect(new_page).to_have_url("https://www.pavantestingtools.com/")
            
            
            
            