# Parabank Automation Testing (Playwright + Python)

This project contained automated UI test scripts for the **parabank** banking application using **playwright** and **python**.
It follows the page object model(POM) structure for maintainability adn scalability.

## Tech Stack

| Tool       | Purpose                   |
|------------|---------------------------|
| Python     | Programming Language      |
| Playwright | UI Automation framework   |
| pytest     | Test runner               |
| Allure     | Test reporting            |


## Project structure

parabank-playwright-python/

├─ config/ # Environment & config files
├─ pages/ # Page Object Model files
├─ reports/ # Test execution reports (ignored in Git)
├─ testdata/ # Test data files
├─ tests/ # conftest and Test cases
└─ utils/ # Helper utilities (logger, fixtures, etc.)