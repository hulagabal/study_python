import pytest
from playwright.sync_api import Playwright

def test_delete_user(playwright: Playwright):
    
    try:
        request = playwright.request.new_context()
        response =request.delete("https://jsonplaceholder.typicode.com/users/1")
        
        assert response.status == 200
        data = response.json() 
        
        assert data == {}
        
    finally:
        request.dispose()    