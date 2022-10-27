#THIS SCRIPT AUTOMATES HUMAN ACTIVITY ON YOUTUBE TO GET EASIER CAPTCHAS VIA GOOGLE

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
import random


#second_set variable will give us the ability to choose between 15 different video options (lines 58-67)
second_set = '//*[@id="contents"]/ytd-video-renderer[' + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) + ']'

email = input("What is your gmail address? \n")
password = input("What is your password? \n")

opts = Options()
opts.add_argument("user-data-dir=C:\\Users\\Joshua\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 12")
#opts.add_argument("--headless")
#opts.add_argument("--window-size=1920x1080")
opts.binary_location = 'C:\\Users\Joshua\AppData\Local\Chromium\Application\chrome.exe'
browser = webdriver.Chrome(executable_path=r'C:\\Users\Joshua\Desktop\chromedriver.exe', chrome_options=opts)

browser.get('https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue')

#Logging into GMAIL account using the input given by user for email and password...

browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
sleep(5)

browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
browser.find_element_by_xpath('//*[@id="passwordNext"]/content').click()

sleep(3)

#Go to YouTube

browser.get('https://youtube.com')
sleep(0.5)
#Setting variables for the first two videos appearing on the homepage (the videos change on every refresh)
vid1 = browser.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[1]')
vid2 = browser.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[2]')

#Python randomly chooses between vid1 and vid2 and the correct video will play based on the selection
if random.choice([vid1 , vid2]) == vid1:
    vid1.click()
else:
    vid2.click()

sleep(100)

#After 100 seconds, go back to homepage

browser.get('https://youtube.com')
#Variables for two potential video search options
opt1 = '30 Minute Timer'
opt2 = '24 Hour Timer'


#Python makes random choice between opt1 and opt2 and will search for the corresponding choice 
if random.choice([opt1 , opt2]) == opt1:
    #Search for opt1 in YouTube search bar
    browser.find_element_by_xpath('//*[@id="search"]').send_keys(opt1)
    browser.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()
    sleep(0.5)
    #Python chooses between the first 15 video results and clicks on its choice 
    browser.find_element_by_xpath(second_set).click()
else:
    #Search for opt2 in YouTube search bar
    browser.find_element_by_xpath('//*[@id="search"]').send_keys(opt2)
    browser.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()
    sleep(5)
    browser.find_element_by_xpath(second_set).click()

#From this point, program will proceed to run with YouTube
#MUST MAKE IT SO THAT ALL VIDEOS ARE MUTED !! !! !! !! !! !! !!
#NoSuchElementException with Headless mode - need to create an exception fix
