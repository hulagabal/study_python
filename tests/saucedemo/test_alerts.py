from playwright.sync_api import Page,expect

def test_alerts_popups(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    print("CURRENT URL:", page.url)
    print("PAGE TITLE:", page.title())
    print("PAGE CONTENT:", page.locator("body").inner_text()[:1500])
    
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