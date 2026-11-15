from playwright.sync_api import Playwright

def test_replace_user(playwright: Playwright):
    try:
        request = playwright.request.new_context()
        
        updated_user = {
        "name": "Mutturaj",
        "username": "mutturaj",
        "email": "mutturaj@example.com"}
        
        response = request.put("https://jsonplaceholder.typicode.com/users/1", data=updated_user)
        
        assert response.status == 200
        
        data = response.json()
        
        assert data["name"] == updated_user["name"]
        assert data["username"] == updated_user["username"]
        assert data["email"] == updated_user["email"]
        
    finally:
        request.dispose()    