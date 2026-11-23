user1 = {"address": {"city": "Vijayapura"}}

user2 = {"address": {}}

user3 = {"name": "Leanne Graham"}

def get_user_city(user):
    address = user.get("address")
    if address is not None:
        city= address.get("city")
        return city
    return None

print(get_user_city(user1))
print(get_user_city(user2))
print(get_user_city(user3))