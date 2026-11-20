from utils.api_helper import validate_response, validate_status_code

def test_bearer_auth(api_request):
    
    headers = {
    "Authorization": "Bearer my_test_token"
}

    response = api_request.get("https://httpbin.org/bearer", headers=headers)
    
    data = response.json()
        
    validate_response(response, 200)
    
    assert data["authenticated"] is True
    assert data["token"] == "my_test_token"


def test_bearer_auth_missing_token(api_request):

    response = api_request.get("https://httpbin.org/bearer")
    
    validate_status_code(response, 401)


def test_bearer_auth_invalid_token(api_request):
    
    headers = {
    "Authorization": "Bearer "
}

    response = api_request.get("https://httpbin.org/bearer", headers=headers)
    
    validate_status_code(response, 401)
    
def test_bearer_auth_wrong_scheme(api_request):
    headers = {
        "Authorization": "Basic my_test_token"
    }
    
    response = api_request.get("https://httpbin.org/bearer", headers=headers)
    
    validate_status_code(response, 401)