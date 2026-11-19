from utils.api_helper import validate_response

def test_replace_user(user_client):
    payload = {
        "name": "Ananya Sharma",
        "email": "ananya.sharma@example.com"
    }
    
    response = user_client.replace_user(1, payload)
    validate_response(response, 200)
    
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]