
def test_create_user(api_request):

    user_data = {
    "name": "Mutturaj",
    "username": "mutturaj",
    "email": "muttu@example.com"
}
    
    response = api_request.post("/users", data=user_data)
    assert response.status == 201
    
    data = response.json()
     
    assert data["name"] == user_data["name"]
    assert data["username"] == user_data["username"]
    assert isinstance(data["id"], int)
    assert data["email"] == user_data["email"]