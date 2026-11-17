import pytest

from playwright.sync_api import expect

from pages.inventories_page import InventoriesPage
from pages.products_cart_page import ProductCartPage

from test_data.login_users import LOGIN_USERS
from test_data.products import PRODUCTS

@pytest.mark.parametrize("product_name, product_price",PRODUCTS)
def test_specific_product(logged_in_user, product_name: str, product_price: str):
    
    inventories_page = InventoriesPage(logged_in_user, product_name, product_price)
    inventories_page.verify_product_details()
    inventories_page.verify_add_product_to_cart()
    inventories_page.open_cart_page()

    product_cart_page = ProductCartPage(logged_in_user, product_name, product_price)
    product_cart_page.verify_cart_details()
    product_cart_page.remove_item_from_cart()
    product_cart_page.verify_cart_is_empty()


@pytest.mark.parametrize(
    "logged_in_user", LOGIN_USERS,
    indirect= True,
    ids=[
        "standard_user",
        "problem_user"   
    ]
)    
def test_invetory_page(logged_in_user):
    expect(logged_in_user).to_have_url("https://www.saucedemo.com/inventory.html")    