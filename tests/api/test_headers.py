from playwright.sync_api import Playwright

def test_headers(playwright: Playwright):
    try:
        request = playwright.request.new_context(
            extra_http_headers={
                "X-Test-Client": "Playwright"
            }
        )
        
        response = request.get("https://httpbin.org/headers")
        assert response.status == 200
        data = response.json().get("headers", {}).get("X-Test-Client")
        assert data == "Playwright"
        
    finally:
        request.dispose()
        
def test_bearer(playwright: Playwright):
    token = "demo-token-123"
    try:
        request = playwright.request.new_context(
            extra_http_headers={
                "Authorization": f"Bearer {token}"
            }
        )
        
        response = request.get("https://httpbin.org/bearer")
        assert response.status == 200
        data = response.json()
        assert data["authenticated"] is True
        assert data["token"] == token
    
    finally:
        request.dispose()            
        
def test_bearer_without_token(playwright: Playwright):
    try:
        request = playwright.request.new_context()
        response = request.get("https://httpbin.org/bearer")
        assert response.status == 401
    
    finally:
        request.dispose()        