# Playwright Automation Project

## Description
Python scripts using Playwright to automate login, OTP entry, dashboard navigation, and task creation in a web app. Sensitive credentials and actual URLs are removed.

## Setup

1. Create a Python virtual environment (venv)
2. Activate it
3. Install dependencies: pip install -r requirements.txt
4. Replace the placeholders in the script before running locally:
page.fill("#username", "your_email_here")
page.fill("#password", "your_password_here")
   Used "123456" for otp
insert actual url in page.goto()

## Running the automation
Run `python main.py` in your activated environment.

## Notes
- Browser stays open for inspection; close manually.
