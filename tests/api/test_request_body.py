from utils.api_helper import validate_response

def test_request_body(api_request):
    payload = {
    "name": "Mutturaj",
    "role": "QA",
    "email": "muttu@example.com"
}
    response = api_request.post("https://httpbin.org/post", data=payload)
    
    validate_response(response, 200)
    
    assert payload == response.json()["json"]