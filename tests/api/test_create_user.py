from utils.api_helper import validate_response

def test_create_user(user_client):

    payload = {    
        "name": "Ananya",
        "email": "ananya@example.com"
    }
    
    response = user_client.create_user(payload)
    
    validate_response(response, 201)
    
    data = response.json()
    
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert isinstance(data["id"], int)