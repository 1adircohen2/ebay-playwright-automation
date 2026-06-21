# eBay E2E Automation Project

**Developed by:** Adir Cohen

## Project Overview

This project provides an automated End-to-End (E2E) testing solution for the eBay platform. It simulates a user journey that includes:
- Searching for products.
- Filtering results based on specific price criteria.
- Navigating and collecting multiple product items.
- Adding items to the shopping cart while handling dynamic site variants (size/color).
- Validating the cart subtotal against a predefined budget.

### Test Flow

```mermaid
graph TD
    A[Start] --> B[Login/Session Auth]
    B --> C[Search: 'shoes']
    C --> D{Items Found?}
    D -- No --> E[End Test]
    D -- Yes --> F[Collect URLs]
    F --> G[Loop: Add Items to Cart]
    G --> H[Open Cart Page]
    H --> I[Validate Total <= Budget]
    I --> J[End Test]


