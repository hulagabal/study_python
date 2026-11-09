from pathlib import Path
from playwright.sync_api import Page, expect

def test_file_download(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")
    
    with page.expect_download() as download_info:
        page.get_by_role("link", name="sample.pdf").click()
    
    download = download_info.value
    file_name = download.suggested_filename
    
    download_dir = Path("downloads")
    download_dir.mkdir(parents=True, exist_ok=True)
    
    download_path = download_dir / file_name
    download.save_as(download_path)
    
    assert download_path.exists()
    assert download_path.name == file_name