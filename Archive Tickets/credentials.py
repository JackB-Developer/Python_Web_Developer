

# Logs into Wealth
def WealthLogin():
    loginBox = driver.find_element_by_xpath('//*[@id="email"]').send_keys('jboles@bluelinevoip.com')
    passBox = driver.find_element_by_xpath('//*[@id="password"]').send_keys('Hunter3259')
    loginBtn = driver.find_element_by_xpath('//*[@id="submitloading"]').click()
    sleep(2)