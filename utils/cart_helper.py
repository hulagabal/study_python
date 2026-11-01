from playwright.sync_api import expect

def verify_cart_remove_button(cart_item, product_name):
    cart_item_row = cart_item.filter(has_text=product_name)
    
    expect(cart_item_row).to_have_count(1)
    expect(cart_item_row.get_by_role("button", name= "Remove"), message= f'Product {product_name}: Remove button not visible').to_be_visible()