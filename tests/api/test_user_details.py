import pytest

@pytest.mark.parametrize(
    "user_id, expected_name",
    [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch")
     ],
    ids=[
        "user_1",
        "user_2",
        "user_3"
    ]
)
def test_data_driven_users(api_request, user_id, expected_name):
    
    response = api_request.get(f"/users/{user_id}")
    
    assert response.status == 200
    
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == expected_name
    