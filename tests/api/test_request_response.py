from utils.api_helper import validate_status_code, validate_content_type

def test_request_response(api_request):
    
    user_data = {
    "name": "Mutturaj",
    "username": "mutturaj",
    "email": "muttu@example.com"
    }
    
    response = api_request.post("https://httpbin.org/post", data=user_data)
    
    validate_status_code(response,200)
    validate_content_type(response,"application/json")
    
    
    data = response.json()
    received_data = data["json"]
    assert received_data == user_data