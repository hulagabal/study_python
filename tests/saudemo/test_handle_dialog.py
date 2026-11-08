from playwright.sync_api import sync_playwright

def test_handle_alert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        
        page.goto("https://testautomationpractice.blogspot.com/") # Example page with JS alerts

        
        def handle_dialog(dialog):
            print(f"Dialog type: {dialog.type}")       # "alert", "confirm", or "prompt"
            print(f"Dialog message: {dialog.message}") # The text inside the popup
            
            # You can handle different dialog types accordingly:
            if dialog.type == "prompt":
                # For prompt boxes, you can send text back
                dialog.accept("Hello from Playwright!")
            else:
                # For alert or confirm, you can accept (click OK) or dismiss (click Cancel)
                dialog.accept() # Use dialog.dismiss() if you want to click Cancel

        page.on("dialog", handle_dialog)

        page.get_by_role("button", name="Confirmation Alert").click() # Clicking an element that triggers window.alert()

        browser.close()
        
        
    
    
    
        
   