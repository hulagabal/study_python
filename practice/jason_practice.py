import json
from pathlib import Path

file_path = Path("test_data/customer.json")

with open(file_path, 'r', encoding= "utf-8") as file:
    customers = json.load(file)

for customer in customers:
    print(f"{customer["customerName"]} = {customer["address"]["city"]}")    