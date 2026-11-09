from pathlib import Path

from playwright.sync_api import Page, expect

def test_file_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    
    file_path = Path("test_data/athagry.pdf")
    
    page.locator("#file-upload").set_input_files(file_path)
    page.locator("#file-submit").click()
    
    expect(page.locator("#uploaded-files")).to_have_text("Athagry.pdf")
       