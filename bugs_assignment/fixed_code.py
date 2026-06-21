from playwright.sync_api import sync_playwright, expect
import time

def test_search_functionality():
    # Fix: Using context manager for proper lifecycle management
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # Basic wait/action
        search_box = page.locator("#search")
        search_box.fill("playwright testing")
        
        # Click action
        page.locator(".button").click()
        
        # Validation (Assertion) - Fix: Ensuring the test actually tests something
        results = page.locator(".result-item").first
        expect(results).to_be_visible()
        
        browser.close()
