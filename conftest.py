from pathlib import Path
from datetime import datetime

import pytest
import pytest_html
import base64

from playwright.sync_api import Playwright, Page, Browser, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_Information_page import CheckoutInformationPage
from utils.dialog_helper import handle_dialog
from api.user_client import UserClient


import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL" or "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="function")
def logged_in_user(page, request):
    username, password = getattr(
        request,
        "param",
        ("standard_user", "secret_sauce")
    )
    login_page = LoginPage(page)
    login_page.login(username, password)
    
    yield page
        
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
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        
        if page:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = screenshot_dir / f"{item.name}_{timestamp}.png"
            page.screenshot(path=file_name)
            
            image_data = base64.b64encode(file_name.read_bytes()).decode("utf-8")
            
            extras = getattr(report, "extras", [])
            extras.append(
                pytest_html.extras.image(image_data, mime_type="image/png")
                )
            report.extras = extras
        
    
@pytest.fixture(scope="function")
def checkout_info_page(page:Page) -> CheckoutInformationPage:
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
        
    inventory_page = InventoryPage(page)
    inventory_page.verify_product_details("Sauce Labs Fleece Jacket", "$49.99")
    inventory_page.add_product_to_cart()
    inventory_page.open_cart_page()
        
    cart_page = CartPage(page)
    cart_page.verify_cart_details()
    cart_page.click_checkout()
        
    checkout_information_page = CheckoutInformationPage(page)
    return checkout_information_page

@pytest.fixture(scope="function")
def authenticated_page(browser: Browser, setup_authentication):
    #picks up json file saved by setup authentication fixture
    auth_context = browser.new_context(storage_state="auth.json")
    auth_page = auth_context.new_page()
    try:
        yield auth_page
    finally:
        auth_context.close()
    
@pytest.fixture(scope="session")
def setup_authentication(browser: Browser):
    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        
        expect(page.locator(".inventory_list")).to_be_visible()
        #stores then auth.json
        context.storage_state(path="auth.json")
    
    
        yield
    finally:
        context.close()
 
@pytest.fixture(scope= "function")   
def api_request(playwright: Playwright):
    
    assert base_url, "API_BASE_URL is not configured"
    
    request = playwright.request.new_context(
        base_url=base_url
    )
    try:
        yield request
    finally:    
        request.dispose()

@pytest.fixture
def user_client(api_request):
    return UserClient(api_request)
                    