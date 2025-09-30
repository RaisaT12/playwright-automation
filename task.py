
def create_task(page):
    subject_input = page.locator('input#subject')
    subject_input.wait_for(state='visible', timeout=20000)
    subject_input.scroll_into_view_if_needed()
    subject_input.click()
    subject_input.type("Contact Someone", delay=100)

    desc_input = page.locator('textarea#description')
    desc_input.wait_for(state='visible', timeout=20000)
    desc_input.scroll_into_view_if_needed()
    desc_input.click()
    desc_input.type("Send an email to someone.", delay=100)

    priority_button = page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/form/div/div/div[1]/div[2]/button/span')
    priority_button.wait_for(state='visible', timeout=20000)
    priority_button.scroll_into_view_if_needed()
    priority_button.click()

    option = page.locator('div[role="option"] >> text="Send an Email"')
    option.wait_for(state='visible', timeout=20000)
    option.scroll_into_view_if_needed()
    option.click()

    assign = page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/form/div/div/div[1]/div[3]/button')
    assign.wait_for(state='visible', timeout=20000)
    assign.scroll_into_view_if_needed()
    assign.click()

    asoption = page.locator('body > div.bg-white.dark\\:bg-gray-900.border.border-gray-200.dark\\:border-gray-700.rounded-md.shadow-lg.overflow-hidden > div.max-h-60.overflow-y-auto.py-1 > div')
    asoption.wait_for(state='visible', timeout=20000)
    asoption.scroll_into_view_if_needed()
    asoption.click()

    date_button = page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/form/div/div/div[1]/div[4]/div/div[1]/div/input')
    date_button.wait_for(state='visible', timeout=20000)
    date_button.scroll_into_view_if_needed()
    date_button.click()

    dateoption = page.locator('div[role="option"][aria-label="Choose Thursday, October 2nd, 2025"]')
    dateoption.wait_for(state='visible', timeout=20000)
    dateoption.scroll_into_view_if_needed()
    dateoption.click()

    status_button = page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/form/div/div/div[1]/div[5]/button')
    status_button.wait_for(state='visible', timeout=20000)
    status_button.scroll_into_view_if_needed()
    status_button.click()

    status_option= page.locator('div[role="option"] >> text="In Progress"')
    status_option.wait_for(state='visible', timeout=20000)
    status_option.scroll_into_view_if_needed()
    status_option.click()
    
    reminder_button = page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/form/div/div/div[1]/div[6]/div/div[1]/div/input')
    reminder_button.wait_for(state='visible', timeout=20000)
    reminder_button.scroll_into_view_if_needed()
    reminder_button.click()

    reminder_option = page.locator('div[role="option"][aria-label="Choose Thursday, October 2nd, 2025"]')
    reminder_option.wait_for(state='visible', timeout=20000)
    reminder_option.scroll_into_view_if_needed()
    reminder_option.click()

    related_button=page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/form/div/div/div[1]/div[7]/button')
    related_button.wait_for(state='visible', timeout=20000)
    related_button.scroll_into_view_if_needed()
    related_button.click()

    related_option=page.locator('div[role="option"] >> text="Lead"')
    related_option.wait_for(state='visible', timeout=20000)
    related_option.scroll_into_view_if_needed()
    related_option.click()

    related_select=page.locator('//*[@id="root"]/div/main/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]')
    related_select.wait_for(state='visible', timeout=20000)
    related_select.scroll_into_view_if_needed()
    related_select.click()


    submit_button = page.locator('button[type="submit"]')
    submit_button.wait_for(state='visible', timeout=20000)
    submit_button.scroll_into_view_if_needed()
    submit_button.click()