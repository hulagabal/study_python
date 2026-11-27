# Playwright Python Automation Framework

A Python-based test automation framework built using **Playwright and Pytest** to automate web UI and API testing.

This project demonstrates practical QA automation skills, including:

- End-to-end UI automation using Playwright.
- API testing using Playwright's APIRequestContext.
- Page Object Model (POM) implementation.
- Reusable pytest fixtures for test setup and teardown.
- Data-driven testing and dynamic test data generation.
- Logging, assertions, and test reporting.
- GitHub Actions CI/CD integration.

The framework includes UI and API test scenarios for SauceDemo, Automation Exercise, and JSONPlaceholder.

**Project goal:** Build a maintainable, reusable automation framework that demonstrates real-world software testing practices.
## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | Browser and API automation |
| Pytest | Test execution and test management |
| Pytest-Playwright | Playwright integration with Pytest |
| Requests / APIRequestContext | API testing through Playwright |
| Git & GitHub | Version control and source code management |
| GitHub Actions | CI/CD automation |
| Python Logging | Execution logs and debugging |
| HTML Reports | Test execution reporting |
## Framework Architecture

```text
study_python/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── api/
│   ├── __init__.py
│   └── user_client.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_*.py
│
├── practice/
│   └── Python and automation practice scripts
│
├── test_data/
│   ├── account_data.py
│   ├── api_users.py
│   ├── login_users.py
│   ├── products.py
│   ├── user_schema.py
│   └── Test data files (JSON, CSV, PDF)
│
├── tests/
│   ├── api/
│   ├── saucedemo/
│   ├── the_internet/
│   └── ui/
│
├── utils/
│   ├── api_helper.py
│   ├── cart_helper.py
│   ├── data_generator.py
│   ├── dialog_helper.py
│   ├── logger.py
│   └── pdf_helper.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Folder and File Responsibilities

| Component | Responsibility |
|---|---|
| `api/` | Reusable API client and request methods |
| `pages/` | Page Object Model classes and page interactions |
| `tests/api/` | API testing scenarios
## Features

### UI Automation
- Browser automation using Playwright.
- Page Object Model (POM) implementation.
- Locator strategies using roles, labels, CSS selectors and text.
- Auto-waiting and assertion-based validation.
- Handling alerts, dialogs, popups, tabs and iframes.
- File upload and download validation.
- Tables, dynamic elements and filtering.
- Multi-user authentication and session isolation.
- End-to-end shopping and checkout workflows.

### API Automation
- GET, POST, PUT, PATCH and DELETE requests.
- Request headers, query parameters and authentication.
- API response status and body validation.
- JSON schema and contract validation.
- Positive and negative API testing.
- API request chaining.
- API-based test data creation and cleanup.
- API and UI integration testing.

### Framework Capabilities
- Reusable pytest fixtures.
- Setup and teardown management.
- Data-driven and parameterized testing.
- Dynamic test data generation.
- Centralized logging.
- Reusable helper functions.
- GitHub Actions CI/CD integration.
- Automated test execution and reporting.
## Test Scenarios

### 1. SauceDemo
- User login with valid and invalid credentials.
- Login data parameterization.
- Product selection and filtering.
- Adding single and multiple products to cart.
- Checkout information validation.
- Checkout overview and order completion.
- Dialog handling and browser interactions.

### 2. The Internet
- Basic authentication.
- Cookies and authentication state.
- Multi-user authentication.
- Session isolation.
- Dynamic content and loading.
- JavaScript alerts and dialogs.
- Iframe interactions.
- File upload and download.
- Popup windows and multiple tabs.
- Table filtering.
- CSV-based parameterized tests.

### 3. API Testing — JSONPlaceholder
- User retrieval and creation.
- User updates and deletion.
- Query parameters and custom headers.
- Authentication and authorization.
- Request and response validation.
- JSON schema and contract validation.
- API request chaining.
- Positive and negative scenarios.

### 4. API Testing — Automation Exercise
- Account creation.
- Login verification.
- Account deletion.
- API-created test account used for UI login.
- End-to-end shopping workflow with cart validation and API cleanup.
## Installation and Setup

### Prerequisites

Make sure the following are installed:

- Python 3.10 or later
- Git
- Visual Studio Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/hulagabal/study_python.git
cd study_python
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```bash
playwright install
```

### 6. Run the Tests

```bash
pytest
```
## Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run API Tests

```bash
pytest tests/api/ -v
```

### Run UI Tests

```bash
pytest tests/ui/ -v
```

### Run SauceDemo Tests

```bash
pytest tests/saucedemo/ -v
```

### Run The Internet Tests

```bash
pytest tests/the_internet/ -v
```

### Run a Specific Test File

```bash
pytest tests/api/test_get_user.py -v
```

### Run Tests Matching a Keyword

```bash
pytest -k "login" -v
```

### Run Tests with Browser Visible

```bash
pytest tests/ui/ --headed -v
```
## Pytest Configuration and Logging

The framework uses `pytest.ini` for centralized test configuration.

### Custom Pytest Markers

| Marker | Purpose |
|---|---|
| `smoke` | Critical functionality tests |
| `regression` | Regression test cases |
| `negative` | Negative test scenarios |
| `slow` | Tests that take longer to execute |
| `api` | API tests |

### Logging

- Live logging enabled during test execution.
- INFO logging level.
- Centralized log format with timestamp, log level, logger name and message.
- Helps with debugging and tracking test execution.
## CI/CD Integration

The project uses **GitHub Actions** to automatically execute Playwright tests.

### Workflow Triggers

The workflow runs on:

- Push to the `main` branch.
- Pull requests targeting the `main` branch.
- Manual execution using GitHub Actions (`workflow_dispatch`).

### CI Environment

- Operating System: Ubuntu 24.04
- Python Version: 3.14
- Browser: Chromium
- Test Framework: Pytest
- API Base URL: JSONPlaceholder

### Pipeline Execution

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Playwright and Chromium browser dependencies.
5. Executes the pytest test suite.
6. Generates a self-contained HTML test report.
7. Uploads the HTML report as a GitHub Actions artifact.

### Test Reporting

The HTML report is generated at:

```text
reports/report.html
```

The report is uploaded as a GitHub Actions artifact named:

```text
playwright-html-report
```

The report upload step runs even when tests fail, allowing test results to be inspected after unsuccessful pipeline executions.

To access the report:

1. Open the GitHub repository.
2. Navigate to the Actions tab.
3. Select a workflow run.
4. Find the Artifacts section.
5. Download `playwright-html-report`.
## Future Improvements

The framework will continue to evolve with improvements in automation coverage, reliability and maintainability.

Planned enhancements include:

- Expand cross-browser testing to Firefox and WebKit.
- Improve test execution parallelization.
- Enhance HTML reporting and test result analysis.
- Add more API and UI integration scenarios.
- Improve test data management and environment configuration.
- Strengthen framework reliability and flaky test investigation.
- Explore AI-assisted QA automation capabilities.

## Author

**Mutturaj Hulagabal**

QA Automation Engineer | Playwright | Python | API Testing

GitHub: [hulagabal](https://github.com/hulagabal)

Repository: [study_python](https://github.com/hulagabal/study_python)
