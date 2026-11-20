from utils.api_helper import validate_response

def test_combined_request(api_request):
    params = {
    "source": "Playwright",
    "version": "1"
}
    
    headers = {
    "X-Test-Client": "Playwright"
}
    
    payload = {
    "name": "Mutturaj",
    "role": "QA"
}
    response = api_request.post("https://httpbin.org/post", params=params, headers=headers, data=payload)
    
    data = response.json()
    validate_response(response, 200)
    
    assert data["args"] == params
    assert headers["X-Test-Client"] == data["headers"]["X-Test-Client"]
    assert data["json"] == payload