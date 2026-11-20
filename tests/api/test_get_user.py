import pytest
from utils.api_helper import validate_response, validate_status_code
from utils.logger import get_logger
import logging

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