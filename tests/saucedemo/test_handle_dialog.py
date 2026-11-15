from playwright.sync_api import Page

def test_handle_alert(page:Page):
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