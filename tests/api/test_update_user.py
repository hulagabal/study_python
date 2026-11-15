from playwright.sync_api import Playwright

def test_update_user(playwright: Playwright):
    try:
        
        
        request = playwright.request.new_context()
        updated_data = { "email": "mutturaj@example.com" }
        
        response = request.patch("https://jsonplaceholder.typicode.com/users/1", data=updated_data)

        assert response.status == 200
        
        data = response.json()
        
        print(data)
        
        assert data["email"] == updated_data["email"]
        assert data["username"] == 'Bret'
        
    finally:
        request.dispose()    
    