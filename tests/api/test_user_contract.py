import pytest

from test_data.user_contract import USER_CONTRACT, USER_NESTED_CONTRACT, OPTIONAL_USER_CONTRACT
from utils.api_helper import validate_response, validate_response_data, validate_optional_field_types, validate_optional_non_empty_fields, validate_field_types

def test_get_user(user_client):
    response = user_client.get_user(1)
    validate_response(response, 200)
    data = response.json()
    validate_response_data(data=data, required_fields= list(USER_CONTRACT.keys()), expected_types= USER_CONTRACT,nested_fields=USER_NESTED_CONTRACT)
    
    
def test_optional_field_type_missing_phone():
    user_missing_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
        }          
    
    validate_optional_field_types(user_missing_phone,OPTIONAL_USER_CONTRACT)


def test_optional_field_type_user_valid_phone():       
    
    user_valid_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": "1-770-736-8031"
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


def test_optional_phone_valid():
    user_null_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": "1234567890"
    }
        
    validate_optional_field_types(user_null_phone, OPTIONAL_USER_CONTRACT)
    validate_optional_non_empty_fields(user_null_phone, OPTIONAL_USER_CONTRACT)


def test_nullable_edge_cases_blank():
    user_null_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": ""
    }
        
    with pytest.raises(AssertionError):
        validate_optional_non_empty_fields(user_null_phone, OPTIONAL_USER_CONTRACT)


def test_nullable_edge_cases_white_space():
    user_null_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": "    "
    }
        
    with pytest.raises(AssertionError):
        validate_optional_non_empty_fields(user_null_phone, OPTIONAL_USER_CONTRACT) 


def test_nullable_edge_cases_none():
    user_null_phone = {
        "id": 1,
        "name": "Leanne Graham",
        "phone": None
    }
        
    with pytest.raises(AssertionError):
        validate_optional_non_empty_fields(user_null_phone, OPTIONAL_USER_CONTRACT)

        
def test_optional_phone_missing():
    user = {"id": 1, "name": "Leanne Graham"}
    validate_optional_non_empty_fields(user, OPTIONAL_USER_CONTRACT)

    
def test_id_true():
    user = {
        "id": True,
        "name": "Leanne Graham",
        "email": "leanne@example.com",
        "username": "Bret"
    }
        
    with pytest.raises(AssertionError):
        validate_field_types(user,USER_CONTRACT)

        
def test_id_123():
    user = {
        "id": 123,
        "name": "Leanne Graham",
        "email": "leanne@example.com",
        "username": "Bret"
    }
    
    validate_field_types(user,USER_CONTRACT)        


def test_id_str123():
    user = {
        "id": "123",
        "name": "Leanne Graham",
        "email": "leanne@example.com",
        "username": "Bret"
    }
        
    with pytest.raises(AssertionError):
        validate_field_types(user,USER_CONTRACT)


def test_id_none():
    user = {
        "id": None,
        "name": "Leanne Graham",
        "email": "leanne@example.com",
        "username": "Bret"
    }
        
    with pytest.raises(AssertionError):
        validate_field_types(user,USER_CONTRACT)                                