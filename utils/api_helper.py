from utils.logger import get_logger

logger = get_logger(__name__)

def validate_status_code(response, expected_status, endpoint="Unknown endpoint"):
        
    if response.status != expected_status:
        logger.error(
            "API status validation failed | %s | Expected: %s | Actual: %s",
            endpoint,
            expected_status,
            response.status,
        )
        
    assert response.status == expected_status, (
        f"Expected status {expected_status}, "
        f"but received {response.status}"
        )
    
def validate_content_type(response, expected_type):
    content_type = response.headers.get("content-type", "")

    if expected_type not in content_type:
        logger.error(
            "Content-Type validation failed | Expected: 'application/json' | Actual: '%s' | Headers: %s",
            content_type,
            content_type
        )
        
    assert expected_type in content_type, (
            f"Expected content type {expected_type}, "
            f"but received {response.headers['content-type']}"
        )

def validate_response(response, expected_status, endpoint="Unknown endpoint"):
    validate_status_code(response, expected_status, endpoint)
    validate_content_type(response, "application/json")
    

def validate_required_fields(data, required_fields):
    
    for field in required_fields:
        assert field in data,  f"Required field '{field}' is missing"

def validate_non_empty_fields(data, required_fields):
    
    for field in required_fields:
        
        assert data[field] is not None, f"{field} cannnot be None"
        
        if isinstance(data[field], str):
            stripped = data[field].strip()
            
            assert stripped != "", f"{field} cannot be empty"


def validate_field_types(data, expected_types):
    
    for field, expected_type in expected_types.items():
        if not isinstance(data[field], expected_type):    
            raise AssertionError(
                f"Expected {expected_type.__name__}, "
                f"but received {type(data[field]).__name__}"
                )


def validate_response_data(data, fields, types, positive_integer_fields=None, nested_fields=None):
    validate_required_fields(data, fields)
    validate_non_empty_fields(data, fields)
    validate_field_types(data, types)
    if positive_integer_fields is not None:
        for field in positive_integer_fields:
            validate_positive_integer(data[field], field)
    
    if nested_fields is not None:
        validate_nested_fields(data, nested_fields)        

user = {
    "id": -5,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "leanne@example.com"
}
def validate_positive_integer(value, field_name):
    
    if type(value) is not int:
        raise AssertionError(f"{field_name} must be an integer, received {value}")
    
    if value <= 0:
        raise AssertionError(f"{field_name} must be positive, received {value}")
         
                
def validate_numeric_range(value, field_name, minimum, maximum):
    
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        message = f"{field_name} is not numeric"
        raise AssertionError(message)
    
    if value < minimum or value > maximum:
        message = f"{field_name} is out of range and allowed range is {minimum}, {maximum}"
        raise AssertionError(message)    

def validate_string_length(value, field_name, minimum, maximum):
    
    if not isinstance(value, str):
        message = f"{field_name} must be string"
        raise AssertionError(message)
    
    
    if len(value) < minimum or len(value) > maximum:
        message = f"{field_name} length must be in range between {minimum} and {maximum}"
        raise AssertionError(message)    
        
def validate_product_data(product):
    # Validate product ID
    validate_positive_integer(product["id"], "ID")
    # Validate product name
    validate_string_length(product["name"], "Product Name",maximum=50, minimum=3)
    # Validate product price
    validate_numeric_range(product["price"], "Price", minimum=1, maximum=200000)
    # Validate product quantity
    validate_positive_integer(product["quantity"], "Quantity")
    validate_numeric_range(product["quantity"], "Quantity", minimum=1,  maximum=100)
    # Validate product SKU
    validate_string_length(product["sku"], "SKU", minimum=5, maximum=5)


def validate_nested_fields(data, nested_fields):
    for parent, fields in nested_fields.items():
        parent_data = data.get(parent) 
        assert parent_data is not None, f"{parent} is missing"
        assert isinstance(parent_data, dict), f"{parent} must be a dictionary"
        
        for field, expected_type in fields.items():
            field_value= parent_data.get(field)
            assert field_value is not None
            assert isinstance(field_value, expected_type), f"{field} must be {expected_type.__name__}"            
                         