# Easy-Captcha-Bot

**Project Created January 2019 via PYTHON**

--> In high school, I was highly involved in buying and reselling popular sneakers, like Yeezys, Jordans, etc.

--> These releases often would go live and sell out very quickly.

--> One thing that would slow me and other buyers down a lot is the possibilty of getting stuck on a very difficult captcha, requiring you to click multiple images, and sometimes with multiple rounds of questions. 

--> I learned from others in the sneaker community and from my own research that a Google account's reCaptcha score level will determine the difficulty of the captcha sent to the user. 

--> If you log into a Google account with a high reCaptcha score, your chances of getting a one-click captcha, where you simply click the box and it submits without asking any questions, is high. 

--> 2 main ways to get a high reCaptcha score is to 1) have an older Google account, and 2) have a Google account that is actively used

--> My Easy Captcha Bot Python Project automates activity on your Google account in order to get easy captchas via Google.




# Random Noun Search (randomnounsearch.py)

I used **Selenium Webdriver** with Python in order to run automated tasks via a browser (I used Google Chrome / Chromium)

--> I imported **exceptions** for Selenium to prevent the code from being interrupted by a situation where a certain element is not yet clickable, for whatever reason

I also imported the **sleep** function to be able to set some necessary delays in the program.

--> The program will first ask for the user's email and password, which the script will then automatically use to log into Google in the browser. Then, it will grab 25 random nouns from a random noun generator site. The script will then take each of these nouns, one by one, and look them up, click on one of the links that come up related to that search, and surf the page for some time. It will run through all 25 nouns, and once it finishes all 25, it will go and pick a new 25 nouns to search. The main while loop will run indefifnitely, until the user manually stops the program. The script ultimately increases activity on your Google account by running endless Google search engine activity, that gives the impression of human activity.



# Youtube (youtube.py)

For this part of the program, I used all the same libraries and tools used in randomnounsearch.py. 

--> The program asks for the user's email and password, which the script then uses to log in. Then, it goes to YouTube. Then, the code randomly chooses between the first and second video on the homepage, and then clicks on its choice. After 100 seconds, it will then return to YouTube homepage. The script then makes a choice between 2 search options: opt1 ("30 Minute Timer") and opt2 ("24 Hour Timer"), and it searches its choice in the YouTube search bar. The script will then choose randomly between the first 15 results that come up, and will click and play the result. From this point, the code runs indefinitely until the user manually exits the program. This script will enable you to increase activity on your Google account by running a lot of YouTube video time. You could use something like this to be harvesting multiple Google accounts simultaneously to get easy captchas.



**I have used my program on Google accounts that were newly created, and it definitely worked to boost my account to a high reCaptcha score with simple, one-click captchas. It's an incredibly useful tool that can surely be made into a legitimate software!**




