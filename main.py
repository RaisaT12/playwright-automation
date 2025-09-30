from playwright.sync_api import sync_playwright
from login import login
from otp import enter_otp
from dashboard import navigate_dashboard
from task import create_task
import time

def start_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
    return p, browser, page


def main():
    p, browser, page = start_browser()
    login(page)
    enter_otp(page)
    navigate_dashboard(page)
    create_task(page)

    print("Automation finished. Browser will stay open. Close manually when done.")
    while True:
        time.sleep(1)  


main()
