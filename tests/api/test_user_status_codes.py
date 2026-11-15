import pytest

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (2, 200),
        (3, 200),
        (999, 404)
    ],
    ids=[
        "valid_user_1",
        "valid_user_2",
        "valid_user_3",
        "nonexistent_user"
    ]   
)
def test_get_user(api_request, user_id, expected_status):
    response = api_request.get(f"/users/{user_id}")
    assert response.status == expected_status