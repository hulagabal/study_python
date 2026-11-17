import json
from pathlib import Path
import pytest


expected_cities = {
    "Ananya Sharma": "Bengaluru",
    "Rohan Verma": "Mumbai"
}

file_path = Path("test_data/customer.json")

with open(file_path, "r", encoding="utf-8") as file:
    customers = json.load(file)

@pytest.mark.parametrize("customer", customers)
def test_customer_details(customer):
    expected_city = expected_cities[customer["customerName"]]
    actual_city = customer["address"]["city"]
    
    assert expected_city == actual_city
    