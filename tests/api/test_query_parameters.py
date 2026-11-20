from utils.api_helper import validate_response

def test_query_parameters(api_request):
    response = api_request.get(
    "https://httpbin.org/get",
    params={
        "name": "Mutturaj",
        "role": "QA"
    }
)
    
    data = response.json()
    validate_response(response, 200)
    
    assert "Mutturaj" in data["args"]["name"]
    assert "QA" in data["args"]["role"]
  