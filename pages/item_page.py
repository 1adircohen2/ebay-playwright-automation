import time
from pages.base_page import BasePage

class ItemPage(BasePage):
    ADD_TO_CART_BUTTON = "#atcBtn_btn_1"
    LISTBOX_CONTROLS = ".listbox-button__control"
    LISTBOX_OPTIONS = "div[role='option']"
    CLOSE_POPUP_BUTTON = "button[aria-label='Close dialog']"

    def add_items_to_cart(self, urls: list) -> None:
        for index, url in enumerate(urls):
            self.navigate(url)
            self.wait_for_load_state()
            

            try:
                buttons = self.page.locator(self.LISTBOX_CONTROLS).all()
                for btn in buttons:
                    if btn.is_visible() and "Select" in btn.inner_text():
                        btn.click()
                        time.sleep(0.5)
                        options = self.page.locator(self.LISTBOX_OPTIONS).all()
                        for opt in options:
                            if "Select" not in opt.inner_text() and opt.is_visible():
                                opt.dispatch_event("click")
                                time.sleep(1)
                                break
            except: pass


            self.page.locator(self.ADD_TO_CART_BUTTON).first.click(force=True)
            try:
                self.page.locator(self.CLOSE_POPUP_BUTTON).first.click()
            except: pass
            self.take_screenshot(f"item_{index+1}_added")
