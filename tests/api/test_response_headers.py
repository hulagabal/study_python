import time

def test_response_headers(api_request):
    
    response = api_request.get("https://httpbin.org/response-headers?X-Test-Header=PlaywrightQA")
    
    print(response.status)
    
    assert response.status == 200
    
    print(response.ok)
    
    assert response.ok is True
    
    print(response.status_text)
    
    print(response.headers)
    
    headers = response.headers
    
    assert "application/json" in headers["content-type"]
    
    assert headers["x-test-header"] == "PlaywrightQA"


def test_response_time(api_request):

    start_time = time.perf_counter()
    response = api_request.get("https://httpbin.org/get")    
    end_time = time.perf_counter()
    
    response_time = (end_time - start_time) * 1000
    
    print(f"Response time: {response_time:.2f}ms" )
    
    assert response.status == 200
    assert response_time < 3000    