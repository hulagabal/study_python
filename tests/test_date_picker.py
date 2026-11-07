from playwright.sync_api import sync_playwright, expect


def test_date_picket_one():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page= browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        
        date_picker1= page.locator("#datepicker")
        date_picker1.fill("04/11/2026")
        expect(date_picker1).to_have_value("04/11/2026")
        
        
        date_picker2 = page.locator("#txtDate")
        date_picker2.click()
        
        page.locator(".ui-datepicker-month").select_option("11")
        page.locator(".ui-datepicker-year").select_option("2027")
        page.locator("a[data-date='14']").click()
        expect(date_picker2).to_have_value("14/12/2027")
        

def test_date_range():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")

        # Locate date inputs
        start_date = page.locator("#start-date")
        end_date = page.locator("#end-date")

        # Select date range
        start_date.fill("2026-11-03")
        end_date.fill("2026-12-07")

        # Submit
        page.locator(".submit-btn").click()

        # Verify selected dates
        expect(start_date).to_have_value("2026-11-03")
        expect(end_date).to_have_value("2026-12-07")
        expect(page.locator("#result")).to_have_text("You selected a range of 34 days.")

        browser.close()