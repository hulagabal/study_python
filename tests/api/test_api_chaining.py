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
    validate_status_code(response_get, 404)
    assert response_get.url.endswith(f"/posts/{post_id}")
    assert response_get.json() == {}


def ttest_get_patch_get_chaining(user_client):
    
    response = user_client.get_user(1)
    
    validate_status_code(response, 200)
    
    data = response.json()
    
    original_name = data["name"]
    print(original_name)
    user_id = data["id"]
    
    payload= {"name": "Mutturaj"}
    response_update = user_client.update_user(user_id, payload=payload)
    
    validate_status_code(response_update, 200)
    
    update_data = response_update.json()
    
    updated_id = update_data["id"]
    
    assert update_data["name"] == "Mutturaj"
    
    response_get = user_client.get_user(updated_id)
    
    validate_status_code(response_get, 200)
    
    get_data = response_get.json()
    assert get_data["name"] == original_name
    
    
   
    
    

    
    
    
            
    