from playwright.sync_api import Page

def test_broken_links(page: Page):    
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    # Locate all links inside the "Broken Links" section
    # Adjust locator to target the links following the 'Broken Links' heading
    broken_links = page.locator("//h4[text()='Broken Links']/following-sibling::a")
    
    count = broken_links.count()
    print(f"Found {count} links to check:\n")

    for i in range(count):
        link = broken_links.nth(i)
        link_text = link.inner_text()
        href = link.get_attribute("href")

        if href:
            # Send an HTTP GET request using Playwright's APIRequestContext
            response = page.request.get(href)
            status = response.status

            if status >= 400:
                print(f"[BROKEN] {link_text} -> {href} (Status: {status})")
            else:
                print(f"[VALID]  {link_text} -> {href} (Status: {status})")