def validate_status_code(response, expected_status):    
    assert response.status == expected_status, (
        f"Expected status {expected_status}, "
        f"but received {response.status}"
        )
    
def validate_content_type(response, expected_type):
    assert expected_type in response.headers["content-type"], (
            f"Expected content type {expected_type}, "
            f"but received {response.headers['content-type']}"
        )

def validate_response(response, expected_status):
    validate_status_code(response, expected_status)
    validate_content_type(response, "application/json")        