import json
from pathlib import Path
import pytest


file_path = Path("test_data/customer.json")

with open(file_path, "r", encoding="utf-8") as file:
    customers = json.load(file)

# Validate test data outside the test function
assert customers, "Customer JSON file must not be empty"    
    
@pytest.mark.parametrize("customer", customers)
def test_create_customer(api_request, customer):
    print(customer)

    response = api_request.post("/posts", data=customer)
    assert response.status == 201
    
    response_data = response.json()
    
    assert response_data["customerName"] == customer["customerName"]
    assert response_data["email"] == customer["email"]
    assert response_data["id"] is not None
    assert response_data["address"]["city"] == customer["address"]["city"]


customer_data = {
    "name": "Ananya"
}

def test_create_customer_negative(api_request):
    response = api_request.post("/posts", data=customer_data)
    print(response.status)
    print(response.json())    