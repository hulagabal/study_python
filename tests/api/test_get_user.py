import pytest
from utils.api_helper import validate_response, validate_status_code

@pytest.mark.api
@pytest.mark.smoke
def test_get_user(user_client):
    response = user_client.get_user(1)
    
    validate_response(response, 200)
    
    data = response.json()
    
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "email" in data

@pytest.mark.negative
def test_get_nonexistent_user(user_client):
    response = user_client.get_user(999)
    
    validate_status_code(response, 404)
    
    data = response.json()
    assert data == {}
        
        
def test_all_users(user_client):
    response = user_client.get_all_users() 

    validate_response(response, 200)

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10

    for user in data:
        assert isinstance(user, dict)
        assert "id" in user
        assert isinstance(user["id"], int)