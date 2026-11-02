from playwright.sync_api import sync_playwright, expect

def test_search_wikipedia():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        page.locator("#Wikipedia1_wikipedia-search-input").fill("India")
        page.locator(".wikipedia-search-button").click()
        
        result = page.locator("#wikipedia-search-result-link a")
        expected_titles=result.all_inner_texts()
        count = result.count()
        
        assert count > 0
        
        for index in range(count):
            expected_url = result.nth(index).get_attribute("href")
            expected_title = expected_titles[index] + " - Wikipedia"
            with page.expect_popup(timeout=30000) as popup_info:
                result.nth(index).click()
    
            new_page = popup_info.value
            
            new_page.wait_for_load_state("domcontentloaded")
            
            expect(new_page).to_have_url(expected_url)
            expect(new_page).to_have_title(expected_title)
            
            new_page.close()