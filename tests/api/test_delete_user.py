def test_delete_user(user_client):
    response = user_client.delete_user(1)
    
    assert response.status == 200