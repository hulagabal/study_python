import pytest

@pytest.mark.smoke
def test_get_user(api_request):
        response = api_request.get("/users/1")
        
        assert response.status == 200
        assert "application/json" in response.headers["content-type"]
        
        data = response.json()
        
        assert isinstance(data["id"], int)
        assert isinstance(data["name"], str)
        
        assert data["id"] == 1
        assert data["name"] == "Leanne Graham"
        assert "email" in data

@pytest.mark.negative
def test_get_nonexistent_user(api_request):
    response = api_request.get("/users/999")
    
    assert response.status == 404
    
    data = response.json()
    assert data == {}
        
        
        