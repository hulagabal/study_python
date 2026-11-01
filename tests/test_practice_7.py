from playwright.sync_api import sync_playwright


def test_common_testing():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        
        
        page.get_by_placeholder("Enter Name").fill("Muttu")
        page.get_by_placeholder("Enter EMail").fill("Hulagabal")
        page.get_by_placeholder("Enter Phone").fill("8970711727")
        
        page.locator("#textarea").fill("Atharga, Indi, Vijayapur 586112")
        
        page.locator("input[value='male']").check()
        page.locator("input[value='sunday']").check()
        page.locator("input[value='saturday']").check()
        
        page.locator("#country").select_option(value="Australia")
        
        
        page.locator("#colors").select_option(value=["Red", "Blue"])
        
        page.locator("#datepicker").fill("10/31/2026")
        
        page.locator("#singleFileInput").set_input_files("C:/Users/mutturaj.h/Downloads/Designation Change Letter-10305.pdf")
        page.get_by_role("button", name="Upload Single File").click()
        print(page.locator("#singleFileStatus").text_content())
        
        page.locator("#pagination").get_by_role("link", name="4").click()
        
        rows=page.locator("#productTable tr").all()
        
        target_id = "17"
        
        for row in rows:
            cells = row.locator("td").all()
            if len(cells) >= 4:
                item_id= cells[0].inner_text().strip()
                print(item_id)
                
                if item_id == target_id:
                    name = cells[1].inner_text().strip()
                    price = cells[2].inner_text().strip()
                    
                    checkbox = cells[3].locator("input[type= 'checkbox']")
                    is_checked=checkbox.is_checked()
                    
                    print(f"ID: {item_id} | Name: {name} | Price: {price}")
                    
                    if not is_checked:
                        checkbox.check()
                    break    
        
        
        table = page.locator("table").filter(has=page.locator("th", has_text="BookName"))
        headers= table.locator("th").all_inner_texts()
        print(f"Table Headers: {headers}")
        assert "BookName" in headers
        assert "Author" in headers
        
        rows= table.locator("tr").all()
        
        table_data= []
        
        for row in rows[1:]:
            cells = row.locator("td").all()
            if len(cells) > 0:
                row_values = [cell.inner_text().strip() for cell in cells]
                table_data.append(row_values)
                                
        
        for item in table_data:
            book_name, author, subject, price = item
            
            if author == "Mukesh":
                print(f"Book Name: {book_name} {subject} price at {price}")
        
        
        