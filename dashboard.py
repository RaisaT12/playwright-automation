def navigate_dashboard(page):
    page.goto("dashboard_link")
    page.wait_for_timeout(5000)
    locator = page.locator('//*[@id="root"]/div/header/div[1]/button')
    locator.wait_for(state='visible', timeout=10000)
    locator.click()


def navigate_task(page):
    locator = page.locator('//*[@id="root"]/div/div[1]/nav/ul[2]/li/a/div')
    locator.wait_for(state='visible', timeout=10000)
    locator.click()
    locator = page.locator('//*[@id="root"]/div/main/div/div[1]/div[2]/button')
    locator.wait_for(state='visible', timeout=10000)
    locator.click()
    page.wait_for_timeout(20000)


def navigate_contact(page):
    locator=page.locator('//*[@id="root"]/div/div[1]/nav/ul[3]/li/a/div/span[2]')
    locator.click()
    locator=page.locator('//*[@id="root"]/div/main/div/div[1]/div[2]/button')
    locator.wait_for(state='visible', timeout=10000)
    locator.click()
    page.wait_for_timeout(20000)
