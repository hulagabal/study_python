from test_data.api_users import VALID_USERS, INVALID_USERS
from utils.api_helper import validate_status_code
import pytest

@pytest.mark.parametrize(
    "user_id,expected_status",
    VALID_USERS,
    ids=["user_1", "user_2", "user_3"]
)
def test_get_valid_users(user_client, user_id, expected_status):
    
    response = user_client.get_user(user_id)
    validate_status_code(response, expected_status)
    
    data = response.json()
    assert data["id"] == user_id, (f"Expected user ID {user_id}, but received {data['id']}")
    
    
@pytest.mark.parametrize(
    "user_id,expected_status",
    INVALID_USERS,
    ids=["invalid_999", "invalid_1000"]
)
def test_get_invalid_users(user_client, user_id, expected_status):
    
    response = user_client.get_user(user_id)
    validate_status_code(response, expected_status)
    
    data = response.json()
    assert data == {}    