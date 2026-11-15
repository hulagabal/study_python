# Study Python 🐍 — Playwright Automation Framework

A practical Python learning and test automation project focused on building reliable UI and API automation using **Playwright and Pytest**.

This repository demonstrates hands-on automation skills, framework design, reusable fixtures, API testing, and real-world web application testing.

## 🚀 Tech Stack

- **Python** — Programming language
- **Playwright** — Browser and API automation
- **Pytest** — Test execution and framework
- **pytest-playwright** — Playwright integration with Pytest
- **Requests** — HTTP requests and link validation
- **Git & GitHub** — Version control

## 📂 Project Structure

```text
study_python/
│
├── pages/                  # Page Object Model classes
│
├── tests/
│   ├── api/                # API automation tests
│   ├── saucedemo/          # SauceDemo UI tests
│   └── the_internet/       # The Internet practice tests
│
├── test_data/              # External test data
│
├── utils/                  # Reusable helper functions
│
├── practice/               # Python and Playwright practice scripts
│
├── downloads/              # Downloaded test files
├── screenshots/            # Failure screenshots
│
├── conftest.py             # Shared fixtures and setup/teardown
├── pytest.ini              # Pytest configuration and markers
├── requirements.txt        # Project dependencies
└── README.md
```

## ✨ Framework Features

### UI Automation
- Browser automation using Playwright.
- Page Object Model (POM).
- Reusable Pytest fixtures.
- Locator strategies and assertions.
- Dropdowns, dialogs, frames and popups.
- File uploads and downloads.
- Dynamic web elements and tables.
- Browser contexts and session isolation.
- Authentication using saved storage state.
- Data-driven and parameterized testing.

### API Automation
- GET, POST, PUT and DELETE requests.
- Request headers and authentication.
- Response status and header validation.
- JSON response validation.
- Positive and negative test scenarios.
- Parameterized API tests.
- Reusable API request fixtures.

### Test Framework
- Function and session-scoped fixtures.
- Fixture setup and teardown using `yield` and `try/finally`.
- Indirect parametrization.
- Pytest markers.
- Failure screenshot capture.
- Reusable helper functions.
- Git-based version control.

## 🛠️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/hulagabal/study_python.git

cd study_python
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

## ▶️ Running Tests

Run the complete test suite:

```bash
pytest tests -v
```

Run tests with a visible browser:

```bash
pytest tests --headed -v
```

Run API tests:

```bash
pytest tests/api -v
```

Run SauceDemo UI tests:

```bash
pytest tests/saucedemo -v
```

Run The Internet tests:

```bash
pytest tests/the_internet -v
```

Run a specific test:

```bash
pytest tests/api/test_get_user.py -v
```

Run tests using markers:

```bash
pytest -m smoke -v
```

```bash
pytest -m "smoke and api" -v
```

## 📊 Test Coverage

**Latest verified execution:**

| Test suite | Passed |
|---|---:|
| API Tests | 24 |
| SauceDemo UI Tests | 37 |
| The Internet Tests | 28 |
| **Total** | **89** |

Latest full-suite result: **89 passed, 0 failed**.

Test count may change as the framework evolves.

## 🔒 Test Data and Generated Files

- Authentication state (`auth.json`) is kept out of Git.
- Downloaded files are stored in `downloads/`.
- Failure screenshots are stored in `screenshots/`.
- Generated files and Python cache files are excluded through `.gitignore`.

## 🎯 Learning Goals

This project is an ongoing practical learning journey focused on:

- Improving Python programming skills.
- Building maintainable automation frameworks.
- Developing UI and API testing expertise.
- Understanding Pytest architecture.
- Practising debugging and test reliability.
- Preparing for CI/CD integration.
- Building a professional QA automation portfolio.

## 🔮 Future Improvements

- HTML test reporting.
- Logging improvements.
- CI/CD integration with GitHub Actions.
- Parallel test execution.
- Advanced API automation.
- Framework-level reporting and debugging.

---

**Learning by building. Testing by understanding. Improving every day.**