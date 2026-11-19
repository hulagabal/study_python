import pytest

@pytest.mark.parametrize(
    "user_id",
    ["999", "1000", "1001"]
)
def test_negative_users(api_request, user_id):
    response = api_request.get(f"/users/{user_id}")
    assert response.status == 404
    assert response.json() == {}


def test_unsupported_method(api_request):
    response = api_request.delete("https://httpbin.org/get")

    print(response.status)
    assert response.status == 405
    
    response_body = response.text()
    print(response_body)
    assert "Method Not Allowed" in response_body
    