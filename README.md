
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-v1.40+-green)
![Allure](https://img.shields.io/badge/Allure-Report-red)
# eBay E2E Automation Project
**Developed by:** Adir Cohen

## Project Overview


This project provides an automated End-to-End (E2E) testing solution for the eBay platform. It simulates a user journey that includes:
- Searching for products.
- Filtering results based on specific price criteria.
- Navigating and collecting multiple product items.
- Adding items to the shopping cart while handling dynamic site variants (size/color).
- Validating the cart subtotal against a predefined budget.

## Technical Architecture
This project is built with a focus on maintainability, scalability, and clean code principles:

- **Framework**: [Playwright](https://playwright.dev/) for Python.
- **Design Pattern**: **Page Object Model (POM)** – Logic is separated into specific page classes (`SearchPage`, `ItemPage`, `CartPage`) to improve code modularity and readability (SRP - Single Responsibility Principle).
- **Data-Driven**: External configuration is managed via `config/config.json`, allowing easy adjustments to search queries, budgets, and environment settings.
- **Reporting**: Integrated with **Allure Reports** to provide detailed, graphical insights into test results, including logs and screenshots for every step.

## Project Structure
- `config/`: Contains the `config.json` for environment and test parameters.
- `pages/`: Page Object Model implementation (BasePage, SearchPage, ItemPage, CartPage).
- `tests/`: Contains the main E2E test suite.

## Prerequisites
Ensure you have **Python 3.9+** installed.

- Install the required dependencies:

`pip install -r requirements.txt`

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


