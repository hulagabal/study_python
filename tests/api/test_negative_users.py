

def test_negative_users(api_request):
    response = api_request.get("/users/999")
    assert response.status == 404
    assert response.json() == {}


def test_unsupported_method(api_request):
    response = api_request.delete("https://httpbin.org/get")

    print(response.status)
    print(response.text)
    print(response.text())
    assert response.status == 405    
    