# Zentist QA Automation Demo

Homework project implementing automated UI tests for [the-internet.herokuapp.com](https://the-internet.herokuapp.com) using Playwright and pytest for QA Automation position at Zentist. 

URL for homework tasks: [[URL](https://docs.google.com/document/d/1XBGf_m08qy0_eHt_FwaEsiExClXB7r3LMukOQvhYq4w/edit?tab=t.0)] 


Used stack:
- Python 3.13
- Playwright
- Pytest


## Installation

1. Clone the repository and create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

4. Create `.env` file from the example:
```bash
cp .env.example .env
```

## Tests

Run all tests:
```bash
python -m pytest tests/ -vvv --log-cli-level=INFO --alluredir=allure-results
```

Run tests for a specific page:
```bash
python -m pytest tests/test_mainPage.py -vvv --log-cli-level=INFO
python -m pytest tests/test_loginPage.py -vvv --log-cli-level=INFO
```

Run a specific test:
```bash
python -m pytest tests/test_mainPage.py::TestMainPage::test_site_is_accessible -vvv
python -m pytest tests/test_loginPage.py::TestLoginPage::test_login_positive_case -vvv
```

## Reports
Script to generate local html link to view test results
```bash
allure serve allure-results
```

![Sample of allure reports](Allure%20reports%20for%20all%20tests.png)