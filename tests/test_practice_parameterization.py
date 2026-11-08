import pytest

from pages.inventories_page import InventoriesPage
from pages.products_cart_page import ProductCartPage

@pytest.mark.parametrize("product_name, product_price", 
                         [("Sauce Labs Fleece Jacket", "$49.99"),
                          ("Sauce Labs Bolt T-Shirt", "$15.99"),
                          ("Sauce Labs Onesie1", "$7.99"),
                          ("Test.allTheThings() T-Shirt (Red)", "$15.99")])
def test_specific_product(logged_in_user, product_name: str, product_price: str):
    
    inventories_page = InventoriesPage(logged_in_user, product_name, product_price)
    inventories_page.verify_product_details()
    inventories_page.verify_add_product_to_cart()
    inventories_page.open_cart_page()

    product_cart_page = ProductCartPage(logged_in_user, product_name, product_price)
    product_cart_page.verify_cart_details()
    product_cart_page.remove_item_from_cart()
    product_cart_page.verify_cart_is_empty()