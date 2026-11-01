
from playwright.sync_api import Page, expect
import pytest

from pages.login_page import LoginPage
 


@pytest.mark.parametrize("username, password, expected_result", 
                         [("standard_user", "secret_sauce", "success"), 
                          ("locked_out_user", "secret_sauce", "locked_out"),
                          ("problem_user", "secret_sauce", "success"),
                          ("performance_glitch_user", "secret_sauce", "success"),
                          ("error_user", "secret_sauce", "sort_error")],
                         ids=["standard_user_login_success", "locked_out_user_login_rejected",
                              "problem_user_login", "performance_glitch_user_login", "sort_error_user_login"])
def test_logins(page: Page, get_captured_messages, username: str, password: str, expected_result: str):
    
    login_page = LoginPage(page)
    login_page.login(username, password)
    
    if expected_result == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.locator(".app_logo")).to_have_text("Swag Labs")
    elif expected_result == "locked_out":
        expect(page.locator(".error-message-container")).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    
    elif expected_result == "sort_error":
        
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.locator(".app_logo")).to_have_text("Swag Labs")
        
        page.locator(".product_sort_container").select_option("hilo")
        
        assert len(get_captured_messages) > 0, "No dialog popup was detected!"
        assert get_captured_messages[0] == "Sorting is broken! This error has been reported to Backtrace."
        
    else:
         raise ValueError(f"Unexpected expected_result value: {expected_result}")
