
def test_request_validation(api_request):
    
    user_data = {
        "name": 123333,
        "username": "mutturaj",
        "email": ""
        }
    
    response = api_request.post("/users", data=user_data)
    print(response.status)