
def test_first_name_required(checkout_info_page):
    checkout_info_page.verify_first_name_rquired_error()

def test_last_name_required(checkout_info_page):
    checkout_info_page.verify_last_name_required_error()

def test_postal_code_required(checkout_info_page):    
    checkout_info_page.verify_postal_code_required_error()

def test_valid_customer_info(checkout_info_page):
    checkout_info_page.enter_valid_customer_info()

def test_cancel_btton(checkout_info_page):    
    checkout_info_page.verify_cancel_return_to_cart()    
