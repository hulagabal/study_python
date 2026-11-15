import requests
from pathlib import Path

from playwright.sync_api import Page

def test_broken_link(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    
    links = page.locator("#broken-links a").all()
    
    broken_links= []
    
    for link in links:
        href = link.get_attribute("href")
        
        try:
            response = requests.head(href, timeout=5, allow_redirects=True)
            if response.status_code >= 400:
                broken_links.append((href, response.status_code))          
            else:
                print(f"valid {href}, status")
        except requests.exceptions.RequestException as e:
            broken_links.append((href, "Connection Error"))          
                
    print(broken_links)
    print(f"Total broken links: {len(broken_links)}")

def test_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    scrolling_drowdown = page.locator(".widget-content #comboBox")
    scrolling_drowdown.click()
    
    page.get_by_text("Item 15", exact=True).click()


def test_double_click(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    
    page.get_by_role("button", name="Copy Text").dblclick()
    
    field2_value =page.locator("#field2").input_value()
    
    assert field2_value == "Hello World!"


def test_download_text_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    
    page.locator("#inputText").fill("This text file content")
    page.get_by_role("button", name="Generate and Download Text File").click()
    
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Text File").click()
        
    download = download_info.value
    
    download_dir = Path("downloads")
    download_dir.mkdir(exist_ok=True)
    file_path = download_dir / "info.text"
    download.save_as(file_path)