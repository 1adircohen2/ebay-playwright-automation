import time
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = "#gh-ac"
    NEXT_PAGE_BUTTON = "a.pagination__next"

    def search_items_by_name_under_price(self, query: str, max_price: float, limit: int = 5) -> list:

 
        self.page.wait_for_selector(self.SEARCH_INPUT, timeout=10000)
        self.page.fill(self.SEARCH_INPUT, query)
        self.page.press(self.SEARCH_INPUT, "Enter")
        self.wait_for_load_state()
        
        valid_urls = []

        while len(valid_urls) < limit:
            links_locator = self.page.get_by_role("link")
            all_links = links_locator.all()        
            for link in all_links:
                if len(valid_urls) >= limit:
                    break
                
                try:
                    href = link.get_attribute("href")
                    if href and "/itm/" in href and href not in valid_urls:
                        
                        valid_urls.append(href)
                except Exception:
                    continue

            if len(valid_urls) >= limit:
                break

            try:
                next_button = self.page.locator(self.NEXT_PAGE_BUTTON)
                if next_button.is_visible() and next_button.is_enabled():
                    next_button.click()
                    self.wait_for_load_state()
                    time.sleep(2)
                else:
                    break
            except Exception:
                break

        print(f"[INFO] נאספו בהצלחה {len(valid_urls)} קישורי מוצרים להמשך התהליך.")
        return valid_urls
