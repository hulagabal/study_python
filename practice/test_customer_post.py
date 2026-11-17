import json
from pathlib import Path
import pytest


file_path = Path("test_data/customer.json")

with open(file_path, "r", encoding="utf-8") as file:
    customers = json.load(file)
    
@pytest.mark.parametrize("customer", customers)
def test_create_customer(api_request, customer):
    print(customer)

    response = api_request.post(
    "/posts",
    data=customer
)
    assert response.status == 201
    
    response_data = response.json()
    
    assert response_data["customerName"] == customer["customerName"]
    assert response_data["email"] == customer["email"]
    assert response_data["id"] is not None
    assert response_data["address"]["city"] == customer["address"]["city"]