from selenium import webdriver
from time import sleep #**SLEEP FUNCTIONS WILL BE HIGHLY NECESSARY BECAUSE OF THE TRAFFIC DELAYS
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
from termcolor import colored



email = input("What is your gmail address? \n")
password = input("What is your password? \n")

opts = Options()
opts.add_argument("user-data-dir=C:\\Users\\Joshua\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 12")
opts.add_argument("--headless")
opts.add_argument("--window-size=1920x1080")
opts.binary_location = 'C:\\Users\Joshua\AppData\Local\Chromium\Application\chrome.exe'
browser = webdriver.Chrome(executable_path=r'C:\\Users\Joshua\Desktop\chromedriver.exe', chrome_options=opts)

#browser.get('https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue')


#browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
#browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
#sleep(5)

#browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
#browser.find_element_by_xpath('//*[@id="passwordNext"]/content').click()

sleep(3)


while True:
    browser.get('https://www.randomlists.com/nouns?qty=25&dup=false')
    noun1 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[1]/span').text
    noun2 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[2]/span').text
    noun3 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[3]/span').text
    noun4 = browser.find_element_by_xpath('html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[4]/span').text
    noun5 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[5]/span').text
    noun6 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[6]/span').text
    noun7 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[7]/span').text
    noun8 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[8]/span').text
    noun9 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[9]/span').text
    noun10 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[10]/span').text
    noun11 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[11]/span').text
    noun12 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[12]/span').text
    noun13 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[13]/span').text
    noun14 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[14]/span').text
    noun15 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[15]/span').text
    noun16 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[16]/span').text
    noun17 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[17]/span').text
    noun18 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[18]/span').text
    noun19 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[19]/span').text
    noun20 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[20]/span').text
    noun21 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[21]/span').text
    noun22 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[22]/span').text
    noun23 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[23]/span').text
    noun24 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[24]/span').text
    noun25 = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li[25]/span').text

    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun2)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun3)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun4)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun5)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun6)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun7)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun8)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun9)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun10)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun11)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun12)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun13)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun14)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun15)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun16)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun17)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun18)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun19)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun20)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun21)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun22)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun23)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun24)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)
    sleep(10)
    browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun25)
    sleep(1)

    while True:
        try:
            browser.find_element_by_class_name('LC20lb').click()
            break
        except ElementNotVisibleException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_a = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_a)
            sleep(1)
        except NoSuchElementException:
            sleep(1)
            browser.get('https://www.randomlists.com/nouns?qty=1&dup=false')
            sleep(3)
            noun1_b = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/ol/li/span').text
            browser.get('https://www.google.com/search?safe=strict&source=hp&ei=dKVsXPqfFO23ggfL4rmwCw&q=' + noun1_b)
            sleep(1)

    sleep(10)
