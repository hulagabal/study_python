from pathlib import Path
from datetime import datetime

import pytest

from playwright.sync_api import Page,Browser

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_Information_page import CheckoutInformationPage
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
    
@pytest.fixture(scope="function")
def checkout_info_page(page:Page) -> CheckoutInformationPage:
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
        
    inventory_page = InventoryPage(page)
    inventory_page.verify_product_details()
    inventory_page.add_product_to_cart()
    inventory_page.open_cart_page()
        
    cart_page = CartPage(page)
    cart_page.verify_cart_details()
    cart_page.click_checkout()
        
    checkout_information_page = CheckoutInformationPage(page)
    return checkout_information_page

@pytest.fixture(scope="function")
def authenticated_page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    context.storage_state(path="auth.json")
    auth_context = browser.new_context(storage_state="auth.json")
    auth_page = auth_context.new_page()
    
    yield auth_page
    
    auth_context.close()