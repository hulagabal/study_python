import pytest

from utils.api_helper import validate_response, validate_status_code, validate_required_fields, validate_non_empty_fields, validate_field_types, validate_response_data, validate_positive_integer, validate_numeric_range, validate_string_length, validate_product_data, validate_nested_fields
from utils.logger import get_logger
from test_data.user_contract import OPTIONAL_USER_CONTRACT

logger = get_logger(__name__)

@pytest.mark.api
@pytest.mark.smoke
def test_get_user(user_client):

    response = user_client.get_user(1)
    validate_response(response, 200, "GET /users/1")
    try:
        data = response.json()
        
        logger.info("Validating user response")
        assert isinstance(data["id"], int)
        assert isinstance(data["name"], str)
        
        assert data["id"] == 1
        assert data["name"] == "Leanne Graham"
        assert "email" in data
    except:
        logger.exception("Unexpected error occurred")
        raise    

@pytest.mark.negative
def test_get_nonexistent_user(user_client):
    response = user_client.get_user(999)
    
    validate_status_code(response, 404, "GET /user/")
    
    data = response.json()
    assert data == {}
        
        
def test_all_users(user_client):
    response = user_client.get_all_users() 

    validate_response(response, 200, "GET /users/")

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10

    for user in data:
        assert isinstance(user, dict)
        assert "id" in user
        assert isinstance(user["id"], int)
        
        
@pytest.mark.parametrize("user_id", [1, 2, 3]) 
def test_retrieve_users_params(user_client, user_id):
    params = {"id": user_id}
    response = user_client.retrieve_users(params)
    
    validate_status_code(response, 200 , "GET /users")
    
    data =  response.json()
    
    assert len(data) > 0
    assert data[0]["id"] == params["id"]

def test_retrieve_users_header(user_client):
    headers = {
    "X-Test-Client": "Playwright",
    "Accept": "application/json"
    }
    
    response = user_client.get_users_with_headers(headers)
    
    validate_status_code(response, 200, "GET /users")
    
    data = response.json()
    
    assert data["headers"]["X-Test-Client"] == "Playwright"


def test_verify_response_fields():
    data = {
        
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
        }
    
    assert "id" in data, "ID field is missing"
    assert "email" in data, "Email field is missing"
    assert data["email"] == "Sincere@april.biz"


def test_malformed_json():
    import json

    response_body = '{"id": 1, "name": "Leanne Graham"'

    with pytest.raises(json.JSONDecodeError) as exc_info:
        json.loads(response_body)
        
    print(str(exc_info.value))
    
    assert "Expecting" in str(exc_info.value)
    
def test_required_fields():
    data = {
        
        "id": 1,
        "name": "Leanne Graham"
        }
    
    with pytest.raises(AssertionError):
        validate_required_fields(data, ["id", "name", "email"])
        validate_non_empty_fields(data, ["id", "name", "email"])


def test_none_fields():
    data = {
        "id": 1,
        "name": None,
        "email": ""
        }
    
    with pytest.raises(AssertionError):
        validate_non_empty_fields(data, ["id", "name", "email"])        
    
def test_empty_fields():
    data = {
        "id": 1,
        "name": "Leanne Graham",
        "email": "  "
    }
    
    with pytest.raises(AssertionError):
        validate_non_empty_fields(data, ["id", "name", "email"])


@pytest.mark.parametrize(
    "user_id",
    [1,2,3],
     ids=["user_1", "user_2", "user_3"]
    )
def test_get_user_required_fields(user_client, user_id):
    
    response = user_client.get_user(user_id)
    
    validate_response(response, 200)
    
    data = response.json()
    validate_required_fields(data, ["id", "name", "username", "email"])
    validate_non_empty_fields(data, ["id", "name", "username", "email"])
                           
def test_get_all_users_required_fields(user_client):
    response =  user_client.get_all_users()
    validate_response(response, 200) 
    
    data = response.json()
    assert len(data) > 0, "No users returned by API"
   
    for user in data:
        validate_required_fields(user, ["id", "name", "username", "email"])
        validate_non_empty_fields(user, ["id", "name", "username", "email"])

expected_types = {
    "id": int,
    "name": str,
    "username": str,
    "email": str
}
def test_get_user_field_types(user_client):
    response = user_client.get_user(1)
    validate_response(response, 200)
    data = response.json()
    
    validate_field_types(data, expected_types)


def test_validate_field_types_invalid_data():
    data = {
    "id": "one",
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "test@example.com"
}

    with pytest.raises(AssertionError):
        validate_field_types(data, expected_types)
            
        
def test_get_user_complete_validation(user_client):
    expected_types = {    
        "id": int,
        "name": str,
        "username": str,
        "email": str
    }
    
    response = user_client.get_user(1)
    validate_response(response, 200)
    
    data = response.json()
    
    validate_response_data(data, ["id", "name", "username", "email"], expected_types,  positive_integer_fields=["id"], optional_fields=OPTIONAL_USER_CONTRACT)
    

def test_get_all_users_complete_validation(user_client):
    expected_types = {    
            "id": int,
            "name": str,
            "username": str,
            "email": str
        }
    required_fields = ["id", "name", "username", "email"]
    
    response = user_client.get_all_users()
    validate_response(response, 200)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "response is empty"
    
    for user in data:
        assert isinstance(user, dict)
        validate_response_data(user, required_fields, expected_types)    

def test_validate_user_collection_invalid_data():
    users = [
    {"id": 1, "name": "Leanne Graham", "username": "Bret", "email": "leanne@example.com"},
    {"id": 2, "name": "Ervin Howell", "username": "Antonette", "email": "ervin@example.com"},
    {"id": "three", "name": "Clementine Bauch", "username": "Samantha", "email": "clementine@example.com"}
    ]
    
    required_fields = ["id", "name", "username", "email"]
    
    expected_types = {
        "id": int,
        "name": str,
        "username": str,
        "email": str
        }
    
    for user in users[:2]:
        validate_response_data(user, required_fields, expected_types)

    with pytest.raises(AssertionError):
        validate_response_data(users[2], required_fields, expected_types)


def test_validate_positive_integer_valid():
    validate_positive_integer(5, "id")
        
@pytest.mark.parametrize("value", [0, -5, "5", 2.5, True])        
def test_validate_positive_integer(value):
    with pytest.raises(AssertionError):
        validate_positive_integer(value, "id")
        
def test_response_data_invalid_id():
    data = {
        "id": -5,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "leanne@example.com"
    }

    required_fields = ["id", "name", "username", "email"]

    expected_types = {
        "id": int,
        "name": str,
        "username": str,
        "email": str
    }

    with pytest.raises(AssertionError):
        validate_response_data(
            data,
            required_fields,
            expected_types,
            positive_integer_fields=["id"]
        )               

def test_numeric_range():
    product = { 
        "quantity": 5
    }
    
    validate_numeric_range(product["quantity"], "quantity", 1, 100)
    
@pytest.mark.parametrize("quantity", [0, 101, "50", True])
def test_numeric_range_invalid(quantity):
    with pytest.raises(AssertionError):
        validate_numeric_range(quantity, "quantity", 1, 100)

@pytest.mark.parametrize("quantity", [1, 100])
def test_numeric_range_boundaries(quantity):
    validate_numeric_range(quantity, "quantity", 1, 100)

def test_string_length():
    validate_string_length("laptop", "laptop", 3, 50)

@pytest.mark.parametrize("product",["PC", "A" * 51, 75000, True])
def test_string_length_invalid(product):
    
    with pytest.raises(AssertionError):
        validate_string_length(product, "Product", 3, 50)

@pytest.mark.parametrize("product",["ABC", "A" * 50])
def test_string_length_boundry(product):
    validate_string_length(product, "Product", 3, 50)
    
def test_product_details():
    
    product = {
        "id": 10,
        "name": "Laptop",
        "price": 75000,
        "quantity": 5,
        "sku": "LAP10"
        }

    validate_product_data(product)

invalid_products = [    
        {'id': 10, 'name': 'PC', 'price': 75000, 'quantity': 5, 'sku': 'LAP10'},
        {'id': 10, 'name': 'Laptop', 'price': 250000, 'quantity': 5, 'sku': 'LAP10'},
        {'id': 10, 'name': 'Laptop', 'price': 75000, 'quantity': 150, 'sku': 'LAP10'},
        {'id': 10, 'name': 'Laptop', 'price': 75000, 'quantity': 5, 'sku': 'AB'},]
@pytest.mark.parametrize("product", invalid_products,ids=["invalid_name", "invalid_price", "invalid_quantity", "invalid_sku"])
def test_invalid_product_details(product):
    
    with pytest.raises(AssertionError) as exc:
        validate_product_data(product)
    
    print(exc.value)                                                   

def test_get_user_nested_address_validation(user_client):
    response = user_client.get_user(1)
    
    validate_response(response, 200)
    data = response.json()
    
    required_fields = ["id", "name"]

    expected_types = {
        "id": int,
        "name": str
    }

    nested_fields = {
        "address": {
            "city": str,
            "zipcode": str
        }
    }
    
    validate_response_data(data, required_fields, expected_types, nested_fields=nested_fields)


def test_get_user_nested_address_validation_invalid():

    invalid_user = {
        "id": 1,
        "name": "Leanne Graham",
        "address": {
            "street": "Kulas Light"
        }
    }

    nested_fields = {
        "address": {
            "city": str,
            "zipcode": str
        }
    }

    with pytest.raises(AssertionError):
        validate_nested_fields(invalid_user, nested_fields)    

def test_get_user_nested_address_validation_city_invalid():
    invalid_user = {    
        "id": 1,
        "name": "Leanne Graham",
        "address": {
            "street": "Kulas Light"
        }
    }
    
    address = invalid_user.get("address")
    assert address is not None
    assert isinstance(address, dict)
    city = address.get("city")
    
    with pytest.raises(AssertionError):
        assert city is not None

def test_get_user_nested_address_invalid_type():
    invalid_user = {    
        "id": 1,
        "name": "Leanne Graham",
        "address": {
            "city": 12345,
            "zipcode": "92998-3874"
        }
    }
    
    nested_fields = {    
        "address": {
            "city": str,
            "zipcode": str
        }
    }
    
    with pytest.raises(AssertionError):
        validate_nested_fields(invalid_user, nested_fields)    