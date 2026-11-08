from playwright.sync_api import sync_playwright,expect

def test_alerts_popups():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page =browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        def handle_dialog(dialog):
            dialog_type = dialog.type
                  
            if dialog_type == "alert":
                dialog.accept()
            
            elif dialog_type == "confirm":
                dialog.dismiss()
            
            elif dialog_type == "prompt":
                dialog.accept("Muttu")
        
        page.on("dialog", handle_dialog)
        
        page.get_by_role("button", name="Simple Alert").click()
        page.get_by_role("button", name= "Confirmation Alert").click()
        page.get_by_role("button", name= "Prompt Alert").click()
        expect(page.get_by_text("Hello Muttu ")).to_be_visible()