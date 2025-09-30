
def login(page):
    page.goto("login_link")
    page.wait_for_timeout(500)
    page.wait_for_selector("#username", timeout=15000)
    page.fill("#username", " ") 
    page.wait_for_selector("#password", timeout=15000)
    page.fill("#password", " ") 
    page.wait_for_selector('button[type="submit"]', timeout=15000)
    page.click('button[type="submit"]')  
    page.wait_for_timeout(5000)