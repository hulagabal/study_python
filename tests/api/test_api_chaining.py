import pytest
from utils.api_helper import validate_status_code

from utils.api_helper import validate_status_code


@pytest.mark.parametrize(
    "user_id", [1,2,3]
)
def ttest_get_api_chaining(api_request, user_id):
    response_user = api_request.get(f"/users/{user_id}")
    
    validate_status_code(response_user, 200)
    
    user_data = response_user.json()
    
    requested_user_id = user_data["id"]
    
    response_post = api_request.get(
        "/posts",
        params={"userId": requested_user_id}
        )
    
    validate_status_code(response_post, 200)
    
    post_data = response_post.json()
    
    assert isinstance(post_data, list)
    assert len(post_data) > 0
    
    for post in post_data:
        assert post["userId"] == user_id
        
def test_post_api_chaining(api_request):
    
    payload = {
    "title": "Learning API Chaining",
    "body": "Practising POST and GET requests",
    "userId": 1
    }
    
    post_response = api_request.post("https://jsonplaceholder.typicode.com/posts", data=payload)
    
    validate_status_code(post_response, 201)
    
    data = post_response.json()
    post_id = data["id"]
    
    response_get = api_request.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    
    print(response_get.status)
    print(response_get.text())
    assert response_get.json() == {}
    
   
    
    

    
    
    
            
    