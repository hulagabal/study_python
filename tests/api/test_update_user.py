def test_update_user(user_client):
    payload = { "email": "mutturaj@example.com" }
    
    response = user_client.update_user(1, payload)
    
    assert response.status == 200
    
    data = response.json()
    
    assert data["email"] == payload["email"]
        