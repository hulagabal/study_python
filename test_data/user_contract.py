USER_CONTRACT = {
    "id": int,
    "name": str,
    "username": str,
    "email": str
}


USER_NESTED_CONTRACT = {
    "address": {
        "city": str,
        "zipcode": str
    }
}

REQUIRED_USER_FIELDS = [
    "id",
    "name",
    "username",
    "email"
]

OPTIONAL_USER_FIELDS = [
    "phone",
    "website"
]

OPTIONAL_USER_CONTRACT = {
    "phone": str,
    "website": str
}