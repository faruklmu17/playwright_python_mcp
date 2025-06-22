from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://faruk-hasan.com/automation/signup.html")
        assert "Sign Up - Automation Practice" in page.title()
        browser.close()

def test_signup_button_exists():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://faruk-hasan.com/automation/signup.html")
        assert page.locator("button[type='submit']").is_visible()
        browser.close()
