import pytest
USER_ROLES = [
    ("admin", 200),
    ("employee", 403)
]

@pytest.mark.parametrize(
    "role, status",
    USER_ROLES
)
def test_authorization(role, status):
    
    actual_status = simulate_delete_employee(role)
    assert actual_status == status


def simulate_delete_employee(role):
    if role == "admin":
        return 200
    return 403