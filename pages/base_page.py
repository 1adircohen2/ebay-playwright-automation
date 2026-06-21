import re
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_load_state(self, state: str = "networkidle"):
        self.page.wait_for_load_state(state)

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshot_{name}.png")

    def parse_price(self, price_text: str) -> float:
        match = re.search(r"[-+]?\d*\.\d+|\d+", price_text)
        if match:
            return float(match.group())
        raise ValueError(f"לא ניתן היה לפענח מחיר מתוך הטקסט: {price_text}")
