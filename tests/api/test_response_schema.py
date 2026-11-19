import pytest
from jsonschema import validate

from test_data.user_schema import user_schema



@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_response_schema(api_request, user_id):
    
    response = api_request.get(f"/users/{user_id}")
    print(response.status)
    assert response.status == 200
    
    data = response.json()
    print(data)
    
    validate(instance=data, schema=user_schema)
    
    validate_user_schema(data)
    
    assert "city" in data["address"]
    assert isinstance(data["address"]["city"], str)
    
    assert "geo" in data["address"]
    assert isinstance(data["address"]["geo"], dict)
    
    assert "lat" in data["address"]["geo"]
    assert isinstance(data["address"]["geo"]["lat"], str)
    
    assert "lng" in data["address"]["geo"]
    assert isinstance(data["address"]["geo"]["lng"], str)
   
def validate_user_schema(data):
    
    validate_field(data, "id", int)
    
    validate_field(data, "email", str)
    
    validate_field(data, "username", str)
    
    validate_field(data, "name", str)
    
    validate_field(data, "address", dict)
    
    validate_field(data["address"], "city", str)
    
def validate_field(data, field, expected_type):
    assert field in data, f"{field} is missing"
    assert isinstance(data[field], expected_type), (f'{field} must be {expected_type.__name__}')
    

     
        