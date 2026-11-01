from pathlib import Path
from datetime import datetime

import pytest

from playwright.sync_api import Page

from pages.login_page import LoginPage
from utils.dialog_helper import handle_dialog


@pytest.fixture(scope="function")
def logged_in_user(page, request):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    yield page
    
    if request.node.rep_call.failed:
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True) 
        time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"test_failure_{time_stamp}.png"
        file_path = screenshot_dir / file_name
        
        page.screenshot(path=file_path)
        
        assert file_path.exists(), f'File {file_path} does not exist'
        
    print("Teardown: Test completed.")

@pytest.fixture(scope="function")
def get_captured_messages(page: Page):
    captured_messages= []
    
    def dialog_callback(dialog):
        handle_dialog(dialog, captured_messages)
                   
    page.on("dialog", dialog_callback)
    try:
        yield captured_messages
    finally:
        page.remove_listener('dialog', dialog_callback)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report )
    