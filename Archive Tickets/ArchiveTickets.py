import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from browser import driver
from credentials import WealthLogin
import easygui


'''
# Logs into Wealth
def WealthLogin():
    loginBox = driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    passBox = driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    loginBtn = driver.find_element_by_xpath('//*[@id="submitloading"]').click()
    sleep(2)
'''

# Switches to Unassigned page
def unassignedTickets():
    unassigned = driver.find_element_by_xpath('//*[@id="menu-scrll"]/li[7]/ul/li[4]/a/span').click()
    sleep(2)

# Archives the ticket    
def archiveTickets():
    sleep(1)
    dropDown = driver.find_element_by_xpath('//*[@id="tblTickets"]/tbody/tr[1]/td[10]/div/button[2]').click()
    archiveTicket = driver.find_element_by_xpath('//*[@id="tblTickets"]/tbody/tr[1]/td[10]/div/ul/li[1]/a').click()
    sleep(1)
    driver.switch_to_alert().accept()
    
# Clears text in search bar
def clearText():
    select = driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(Keys.CONTROL + "a");
    delete = driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(Keys.DELETE);

# Finds Online Tickets
def findOnline():
    onlineAlert = driver.find_element_by_xpath('//*[@id="search-input"]')
    clearText()
    onlineAlert.send_keys('online alert')
    onlineAlert.send_keys(Keys.RETURN)
    sleep(1)
    ticketCount()
    sleep(1)

    while ticketCount != 1:
        try:
            element = driver.find_element_by_xpath('//*[@id="tblTickets"]/tbody/tr[1]/td[10]/div/button[2]')
            archiveTickets()
        except NoSuchElementException:
            findOffline()

# Search tickets by Offline
def findOffline():
    offlineAlert = driver.find_element_by_xpath('//*[@id="search-input"]')
    clearText()
    offlineAlert.send_keys('offline alert')
    offlineAlert.send_keys(Keys.RETURN)
    sleep(3)
    ticketCount()
    while ticketCount != 1:
        try:
            element = driver.find_element_by_xpath('//*[@id="tblTickets"]/tbody/tr[1]/td[10]/div/button[2]')
            archiveTickets()
        except NoSuchElementException:
            findWAN()

# Finds WAN alert Tickets
def findWAN():
    wanAlert = driver.find_element_by_xpath('//*[@id="search-input"]')
    clearText()
    wanAlert.send_keys('alert')
    wanAlert.send_keys(Keys.RETURN)
    sleep(1)
    ticketCount()
    sleep(1)

    while ticketCount != 1:
        sleep(1)
        try:
            element = driver.find_element_by_xpath('//*[@id="tblTickets"]/tbody/tr[1]/td[10]/div/button[2]')
            archiveTickets()
        except NoSuchElementException:
            driver.quit()
            easygui.msgbox("All WAN/Online/Offline Tickets have been Archived", title="All Tickets")
            sleep(5)
            sys.exit()

# Find current ticket count
def ticketCount():
    totalCount = driver.find_element_by_xpath('//*[@id="tickets-count"]')

# Opens Chrome and goes to Wealth Login page
#driver = webdriver.Chrome(PATH)
#driver.get('https://wealth.truechoicetech.com/login')

main_page = driver.current_window_handle
sleep(2)
# Log into Wealth
WealthLogin()
# Click on Unassigned Category
unassignedTickets()
# Search for Online/Offline tickets ONLY and archive them
findOnline()
