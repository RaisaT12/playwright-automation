
def enter_otp(page):
    locator = page.locator('xpath=//*[@id="root"]/div[1]/div[2]/div/div[2]/div')
    locator.wait_for(state="visible", timeout=20000)
    locator.click()
    page.wait_for_timeout(5000)
    otp = " "
    for i, digit in enumerate(otp):
        page.fill(f'#otp-input-{i}', digit)
    page.click('button[type="submit"]')
    page.wait_for_timeout(5000)
