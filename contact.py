def create_contact(page):
    fname=page.locator('input#firstName')
    fname.wait_for(state='visible', timeout=20000)
    fname.click()
    fname.type('Mickey', delay=100)


    lname=page.locator('input#lastName')
    lname.wait_for(state='visible', timeout=20000)
    lname.click()
    lname.type('Mouse', delay=100)


    title=page.locator('//*[@id="root"]/div/main/div/div/div/div/div/form/div[1]/div[2]/div[3]/button')
    title.wait_for(state='visible', timeout=20000)
    title.click()
    option=page.locator('div[role="option"] >> text="Sir"')
    option.wait_for(state='visible', timeout=20000)
    option.scroll_into_view_if_needed()
    option.click()


    email=page.locator('input#email')
    email.wait_for(state='visible', timeout=20000)
    email.click()
    email.type('mick@gmail.com', delay=100)


    phone=page.locator('input#phone')
    phone.wait_for(state='visible', timeout=20000)
    phone.click()
    phone.type('01929384940', delay=100)


    job_title=page.locator('input#jobTitle')
    job_title.wait_for(state='visible', timeout=20000)
    job_title.click()
    job_title.type('CEO', delay=100)


    file_input = page.locator('input[type="file"]')
    file_input.set_input_files("C:/Users/raisa.tarannum/Downloads/gingercat.jpg")


    submit=page.locator('button[type="submit"]')
    submit.wait_for(state='visible', timeout=20000)
    submit.click()
