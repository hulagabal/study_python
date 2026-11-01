from playwright.sync_api import expect
from utils.cart_helper import verify_cart_remove_button
import pytest

def test_verify_cart(logged_in_user):
        
        
    inventory_backpack= logged_in_user.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    inventory_backpack_button = inventory_backpack.get_by_role("button", name="Add to cart")
    inventory_backpack_button.click()
        
    shopping_cart_link = logged_in_user.locator(".shopping_cart_link")
    expect(shopping_cart_link).to_have_text("1")
        
    inventory_bike_light= logged_in_user.locator(".inventory_item").filter(has_text="Sauce Labs Bike Light")
    inventory_bike_light_button = inventory_bike_light.get_by_role("button", name="Add to cart")
    inventory_bike_light_button.click() 
        
        
    expect(shopping_cart_link).to_have_text("2") 
        
    remove_backpack_button = inventory_backpack.get_by_role("button", name= "Remove") 
    remove_backpack_button.click()
        
    expect(shopping_cart_link).to_have_text("1")
        
    shopping_cart_link.click()
        
    cart_item=logged_in_user.locator(".cart_item")        
    expect(cart_item).to_have_count(1)
        
    expect(logged_in_user.locator(".inventory_item_name")).not_to_have_text("Sauce Labs Backpack")
    expect(logged_in_user.locator(".inventory_item_name")).to_have_text(["Sauce Labs Bike Light"])
        
    continue_shoppng_button = logged_in_user.get_by_role("button", name= "Continue Shopping")
    continue_shoppng_button.click()
        
    remove_bike_light_button = inventory_bike_light.get_by_role("button", name= "Remove")
    expect(remove_bike_light_button).to_be_visible()
        
    expect(shopping_cart_link).to_have_text("1")
        
    expect(inventory_backpack_button).to_be_visible()
    inventory_backpack_button.click()
        
    expect(shopping_cart_link).to_have_text("2")
        
    shopping_cart_link.click()
    expect(cart_item).to_have_count(2)
        
    expect(logged_in_user.locator(".inventory_item_name")).to_have_text(['Sauce Labs Bike Light', 'Sauce Labs Backpack'])
        
    verify_cart_remove_button(cart_item, "Sauce Labs Bike Light")
    verify_cart_remove_button(cart_item, "Sauce Labs Backpack")
