import pytest

from test_data.user_contract import USER_CONTRACT, USER_NESTED_CONTRACT, OPTIONAL_USER_CONTRACT
from utils.api_helper import validate_response, validate_response_data, validate_optional_field_types

def test_get_user(user_client):
    response = user_client.get_user(1)
    
    validate_response(response, 200)
    data = response.json()
    validate_response_data(data=data, fields= list(USER_CONTRACT.keys()), types= USER_CONTRACT,nested_fields=USER_NESTED_CONTRACT)
    
    
def test_optional_field_type_missing_phone():
    user_missing_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
        }          
    
    user_valid_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": "1-770-736-8031"
        }
    
    user_invalid_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": 123456789
        }
    
    
    validate_optional_field_types(user_missing_phone,OPTIONAL_USER_CONTRACT)


def test_optional_field_type_user_valid_phone():       
    
    user_valid_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": "1-770-736-8031"
        }
    
    user_invalid_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": 123456789
        }
    
    
    validate_optional_field_types(user_valid_phone,OPTIONAL_USER_CONTRACT)    



def test_optional_field_type_user_invalid_phone():       
    
    user_invalid_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": 123456789
        }
    
    
    with pytest.raises(AssertionError):
        validate_optional_field_types(user_invalid_phone,OPTIONAL_USER_CONTRACT)    