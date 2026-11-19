
def test_user_schema(api_request):
    
    response = api_request.get("/users/1")
    assert response.status == 200
    
    data = response.json()
    print(data)
    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data
    assert "address" in data
    assert "company" in data
    
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)
    assert isinstance(data["address"], dict)
    assert isinstance(data["company"], dict)
    
    street = data.get("address", {}).get("street")
    city = data.get("address", {}).get("city")
    company_name = data.get("company", {}).get("name")
    
    assert isinstance(street, str)
    assert isinstance(city, str)
    assert isinstance(company_name, str)