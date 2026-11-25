from utils.api_helper import validate_response

def test_custom_headers(api_request):    
    headers = {            
        "X-Test-Client": "Playwright"
    }

    response = api_request.get(
        "https://httpbin.org/headers",
        headers=headers
)
    validate_response(response, 200)
    
    data = response.json()
    assert "X-Test-Client" in data["headers"]
    assert "Playwright" == data["headers"]["X-Test-Client"]