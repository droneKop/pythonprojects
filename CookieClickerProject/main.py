"""
This script is implementation of a simple way to increase visibility and boost views of an instagram account.
It will log on to your instagram account, go to a page whose followers you want to follow and then follow them.
Refer to in-line comments for info or customizations
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time


# username = "You can write your username here if you are running this script only locally"
# Or, you can also store your username as Environment variable and call the same
# Or, the below line will prompt you to enter your username everytime you run this code
username =  input("Enter your instagram account username: ")

# password  = "You can write your password here if you are running this script only locally"
# Or, you can also store your password as Environment variable and call the same
# Or, the below line will prompt you to enter your password everytime you run this code
password = input("Enter your instagram account username: ")

# similarAccount  = "You can write the name of the account whose users you want to follow here if you are running this script only locally"
# Or, you can also store your similarAccount as Environment variable and call the same
# Or, the below line will prompt you to enter your similarAccount everytime you run this code
# Last option may be best here if you want to follow users from different accounts everytime
similarAccount = input("Enter your instagram account username: ")



class InstagramFollower:
    def __init__(self):
        # creating a configuration object to customize chrome browser launch
        chrome_options = webdriver.ChromeOptions()
        # browser will stay open after script execution is complete
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        # instagram url
        url = "https://www.instagram.com/"
        self.driver.get(url)
        print("Opening Instagram...")
        self.driver.implicitly_wait(3)

        # userInput = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        userInput = self.driver.find_element(By.XPATH, '// *[ @ id = "loginForm"] / div[1] / div[1] / div / label / input')
        userInput.send_keys(username)
        passInput = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        passInput.send_keys(password)
        logIn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
        logIn.click()
        print("Clicked on login...")
        print("--3 second wait--")
        time.sleep(3)
        print("--Another 5 second wait--")
        time.sleep(5)
        notNow = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        notNow.click()
        print(f"Entered account home page of {username}")
        print("--Another 5 second wait--")
        time.sleep(5)

    def accountSearch(self):
        print("Searching for account")
        newUrl = f"https://www.instagram.com/{similarAccount}/followers"
        self.driver.get(newUrl)
        print("Opening account page")
        print("--6 second wait--")
        time.sleep(6)
        modal = self.driver.find_element(By.XPATH, f"//a[@href='/{similarAccount}/followers/']")
        modal.click()
        print(f"Entered follower page of {similarAccount}")
        print("--Another 5 second wait--")
        time.sleep(5)

    def follow(self):
        print("Started follow")
        # all_buttons = self.driver.find_elements(By.LINK_TEXT, value="Follow")
        # all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="._aano button")
        # followClass = " _aswp _aswr _aswu _asw_ _asx2"
        followButton = "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x6nl9eh.x1a5l9x9.x7vuprf.x1mg3h75.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div > button"

        all_buttons = self.driver.find_elements(By.CLASS_NAME, value=followButton)
        print(all_buttons)
        print("Check your buttons")
        for button in all_buttons:
            try:
                button.click()
                print("--Followed 1 user--")
                print("--2 second wait--")
                time.sleep(2)
                print("Followed successfully")
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

newBot = InstagramFollower()
newBot.login()
newBot.accountSearch()
newBot.follow()


