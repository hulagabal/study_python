import uuid

from test_data.account_data import BASE_USER_DATA
def generate_unique_email():
    uuid_id = uuid.uuid4().hex
    return f"testuser_{uuid_id}@example.com"

def get_account_data():
    email = generate_unique_email()
    return {
        **BASE_USER_DATA,
        "email": email
    }


if __name__ == "__main__":
    account1 = get_account_data()
    account2 = get_account_data()

    print(account1)
    print(account2)

    print(account1 is account2)
    print(account1["email"] == account2["email"])    