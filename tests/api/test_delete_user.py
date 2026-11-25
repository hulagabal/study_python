from utils.api_helper import validate_status_code

def test_delete_user(user_client):
    response = user_client.delete_user(1)
    validate_status_code(response, 200)
    assert response.json() == {}