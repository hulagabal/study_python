
def test_users_array(api_request):
    response = api_request.get("/users")
    assert response.status == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10
    
    for user in data:
        assert isinstance(user, dict)
        assert isinstance(user["id"], int)
        assert isinstance(user["name"], str)
        assert isinstance(user["email"], str)