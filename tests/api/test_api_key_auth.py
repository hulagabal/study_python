from utils.api_helper import validate_response
def test_api_key_auth(api_request):
    
    headers = {
    "X-Api-Key": "my_test_api_key"
}
    
    response = api_request.get("https://httpbin.org/headers", headers=headers)
    
    data = response.json()
    
    validate_response(response, 200)
    
    assert "X-Api-Key" in data["headers"]
    
    assert headers["X-Api-Key"] == data["headers"]["X-Api-Key"]