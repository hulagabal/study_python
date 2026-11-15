

def test_request_response(api_request):
    
    user_data = {
    "name": "Mutturaj",
    "username": "mutturaj",
    "email": "muttu@example.com"
    }
    
    response = api_request.post("https://httpbin.org/post", data=user_data)
    
    assert response.status == 200
    assert "application/json" in response.headers["content-type"]
    
    data = response.json()
    received_data = data["json"]
    assert received_data == user_data