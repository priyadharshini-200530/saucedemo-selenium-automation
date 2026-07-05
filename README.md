# SauceDemo Selenium Automation Framework

A Selenium + pytest test automation framework built using the Page Object Model (POM) design pattern, testing the full user journey on [SauceDemo](https://www.saucedemo.com/) — a demo e-commerce application.

## Tech Stack

- Python 3.10
- Selenium WebDriver
- pytest
- Microsoft Edge (WebDriver managed automatically via webdriver-manager)

## Project Structure

saucedemo-selenium-automation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_end_to_end.py
├── conftest.py
├── requirements.txt
└── README.md

## Test Coverage

| Module | Scenarios Covered |
|---|---|
| Login | Valid login, invalid login (error message validation) |
| Inventory | Add item to cart, remove item, sort by price (low to high) |
| Cart | View cart contents, remove item, navigate to checkout |
| Checkout | Full checkout flow, missing first name / last name / zip code validation |
| End-to-End | Complete purchase journey: login → add to cart → checkout → confirmation |

**Total: 13 automated tests**, covering both positive and negative scenarios.

## Architecture

- **Page Object Model** — each page of the app is a Python class holding its locators and actions, kept separate from test logic.
- **Layered pytest fixtures** — `driver` (browser setup) → `logged_in_driver` (pre-authenticated session) → `cart_page_checkout` (pre-populated cart at checkout), removing repeated setup code across test files.
- **Explicit waits** — `WebDriverWait` is used throughout instead of fixed sleep delays, for reliable and efficient execution.

## Setup

```bash
git clone https://github.com/priyadharshini-200530/saucedemo-selenium-automation.git
cd saucedemo-selenium-automation

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Running Tests

```bash
# Run the full suite
pytest tests/ -v

# Run a single file
pytest tests/test_login.py -v
```

## Test Credentials

Uses SauceDemo's publicly documented demo login:
- Username: `standard_user`
- Password: `secret_sauce`

## Author

**Bandi Priyadharshini** — QA / Test Automation Engineer (Fresher)
[GitHub Profile](https://github.com/priyadharshini-200530)
