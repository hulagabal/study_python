import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
    "lastname, firstname, email, due",
    [
        ("Doe", "Jason", "jdoe@hotmail.com", "$100.00"),
        ("Bach","Frank", "fbach@yahoo.com", "$51.00")
        ],
    )
def ttest_locate_filter_table_rows(page:Page, lastname, firstname, email, due):
    page.goto("https://the-internet.herokuapp.com/tables")
    
    table_1 = page.locator("#table1")
    #Uniquely Identifies the username as it has firstname and lastname, in production applications, a unique customer ID or email address is generally a stronger identifier
    row_details = table_1.locator("tbody tr").filter(has_text = lastname).filter(has_text = firstname)
    
    expect(row_details.locator("td").nth(0)).to_have_text(lastname)
    expect(row_details.locator("td").nth(1)).to_have_text(firstname)
    expect(row_details.locator("td").nth(2)).to_have_text(email)
    expect(row_details.locator("td").nth(3)).to_have_text(due)
    
    
@pytest.mark.parametrize(
    "email , lastname, due",
    [
        ("jsmith@gmail.com", "Smith", "$50.00"),
        ("fbach@yahoo.com", "Bach", "$51.00"),
        ("jdoe@hotmail.com", "Doe", "$100.00"),
        ("tconway@earthlink.net", "Conway", "$50.00")
    ]   
)    
def test_filter_table_Data(page:Page, email, lastname, due):
    page.goto("https://the-internet.herokuapp.com/tables")
    
    table2 = page.locator("#table2")
    row = table2.locator("tbody tr").filter(has_text = email)
    
    expect(row).to_have_count(1)
    expect(row.locator("td").nth(2)).to_have_text(email)
    expect(row.locator("td").nth(0)).to_have_text(lastname)
    expect(row.locator("td").nth(3)).to_have_text(due)