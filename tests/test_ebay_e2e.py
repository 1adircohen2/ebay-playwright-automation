import os
import json
import pytest
import time
from playwright.sync_api import sync_playwright
from pages.search_page import SearchPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage

# פיקסטצ'ר שטוען את נתוני הקלט מקובץ הקונפיגורציה החיצוני
@pytest.fixture(scope="session")
def config_data():
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.json")
    with open(config_path, "r") as f:
        return json.load(f)

# פיקסטצ'ר שמנהל פרופיל דפדפן קבוע (שומר לוגין וקוקיז) לעקיפת חסימות
@pytest.fixture(scope="function")
def browser_page(config_data):
    with sync_playwright() as p:
        user_data_dir = os.path.join(os.path.dirname(__file__), "../.user_data")
        context = p.chromium.launch_persistent_context(
            user_data_dir,
            headless=config_data.get("headless", False),
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="en-US",
            timezone_id="America/New_York",
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = context.pages[0] if context.pages else context.new_page()
        page.set_default_timeout(config_data.get("timeout", 30000))
        
        yield page
        
        context.close()


# טסט ה-E2E הראשי של המערכת

def test_ebay_shopping_cart_e2e(browser_page, config_data):

    base_url = config_data["base_url"]
    search_query = config_data["search_query"]
    max_price = config_data["max_price"]
    limit = config_data["items_limit"]

    search_page = SearchPage(browser_page)
    item_page = ItemPage(browser_page)
    cart_page = CartPage(browser_page)

    # שלב 1: ניווט לאתר
    search_page.navigate(base_url)
    search_page.wait_for_load_state()
    
    # -------------------------------------------------------------------------
    time.sleep(10) 
    # -------------------------------------------------------------------------

    # שלב 2: הפעלת פונקציית החיפוש
    item_urls = search_page.search_items_by_name_under_price(
        query=search_query, 
        max_price=max_price, 
        limit=limit
    )
    
    assert len(item_urls) > 0, f"לא נמצאו פריטים עבור החיפוש '{search_query}'"
    
    item_page.add_items_to_cart(item_urls)
    cart_page.assert_cart_total_not_exceeds(max_price, len(item_urls))
