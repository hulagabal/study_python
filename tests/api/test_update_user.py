from utils.api_helper import validate_response

def test_update_user(user_client):
    payload = { "email": "mutturaj@example.com" }
    
    response = user_client.update_user(1, payload)
    
    validate_response(response, 200)
    
    data = response.json()
    assert data["email"] == payload["email"]