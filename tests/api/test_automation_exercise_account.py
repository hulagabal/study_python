from utils.data_generator import get_account_data

def test_create_account_successfully(automation_exercise_account):
    account_data = automation_exercise_account
    
    email = account_data.get("email")
    password = account_data.get("password")

    assert isinstance(email, str) and email.strip(), "Email must be a non-empty string"
    assert isinstance(password, str) and password.strip(), "Password must be a non-empty string"
    
    

def test_verify_login(automation_exercise_user_client, automation_exercise_account):
    account_data = automation_exercise_account
    
    login_payload = {
        "email": account_data["email"],
        "password": account_data["password"]
    }
    
    login_response = automation_exercise_user_client.verify_login(login_payload)
    
    assert login_response.status == 200
    login_body = login_response.json()
    
    assert login_body["responseCode"] == 200
    assert login_body["message"] == "User exists!"
    
def test_delete_account_successfully(automation_exercise_account):
    account_data = automation_exercise_account
    
    email = account_data["email"]
    password = account_data["password"]
    
    assert isinstance(email, str) and email.strip(), "Email must be a non-empty string"
    assert isinstance(password, str) and password.strip(), "Password must be a non-empty string"
    
    
    
    
    