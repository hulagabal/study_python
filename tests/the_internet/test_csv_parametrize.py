import csv
from pathlib import Path
import pytest
from playwright.sync_api import Page, expect

def load_csv_data(file_path: Path):
    path = Path(__file__).resolve().parents[2] / "test_data" / "customers.csv"
    
    with open(path, mode="r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))

test_data = load_csv_data("customers.csv")

@pytest.mark.parametrize(
    "data",
    test_data,
    ids=lambda data: data["email"]
)
def test_filter_table_Data(page:Page, data: dict):
    page.goto("https://the-internet.herokuapp.com/tables")
    
    table2 = page.locator("#table2")
    row = table2.locator("tbody tr").filter(has_text = data["email"])
    
    expect(row).to_have_count(1)
    expect(row.locator("td").nth(2)).to_have_text(data["email"])
    expect(row.locator("td").nth(0)).to_have_text(data["lastname"])
    expect(row.locator("td").nth(3)).to_have_text(data["due"])    