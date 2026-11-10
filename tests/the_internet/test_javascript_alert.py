from playwright.sync_api import Page, Dialog, expect

def test_javascript_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    js_alert_button = page.get_by_role("button", name="Click for JS Alert")
    
    result_text = page.locator("#result")
    
    def callback_function(dialog: Dialog):
        dialog.accept()
        
    page.on("dialog", callback_function)
    
    js_alert_button.click()
    
    expect(result_text).to_have_text("You successfully clicked an alert")
    
def test_javascript_confirm(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    js_confirm_button = page.get_by_role("button", name="Click for JS Confirm")
    result_text = page.locator("#result")
    
    def callback_function(dialog: Dialog):
        dialog.dismiss()
    
    page.on("dialog", callback_function)
    js_confirm_button.click()
    
    expect(result_text).to_have_text("You clicked: Cancel")
    
def test_javascript_prompt(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    js_prompt_button = page.get_by_role("button", name="Click for JS Prompt")
    result_text = page.locator("#result")
    
    def callback_function(dialog: Dialog):
        assert dialog.message == 'I am a JS prompt' 
        dialog.accept("Muttu")
    
    page.on("dialog", callback_function)
    js_prompt_button.click()
    
    expect(result_text).to_have_text("You entered: Muttu")