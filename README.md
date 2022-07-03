# LV Gov QA Automation

Playwright + Python test automation framework for Latvian gov portal testing.

## Setup

1. Install dependencies:
```bash
pip3 install -r requirements.txt
```

2. Install Playwright browsers:
```bash
python3 -m playwright install
```

## Running Tests

Run all tests:
```bash
pytest
```

Run smoke tests only:
```bash
pytest tests/test_smoke.py -v
pytest -m smoke
```

Run full test suite:
```bash
pytest tests/test_home_page.py -v
```

Run specific marker:
```bash
pytest -m regression
pytest -m critical
```

Run with different browser:
```bash
pytest --browser firefox
pytest --browser webkit
```

Run with visible browser (headed mode):
```bash
pytest --headed
```

Run headless (default):
```bash
pytest
```

Generate HTML report (automatic):
```bash
pytest
```
Report saved to: `reports/report.html`

## Project Structure

```
LV_GOV_QA/
├── pages/              Page Object Models
├── tests/              Test files
├── fixtures/           Test fixtures
├── utils/              Utility functions
├── reports/            Test reports
├── conftest.py         Pytest configuration
└── pytest.ini          Pytest settings
```

## Configuration

Base URL: https://latvija.gov.lv
Browser: Chromium (default)
Viewport: 1920x1080


- meta: README touch (2022-07-03 12:21:53 -0500)
