from tkinter.font import names

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
import time

url = "https://appbrewery.github.io/Zillow-Clone/"
googleFormUrl = "https://forms.gle/tg8yUHRFSYQZXqMM8"

zillowSoup = BeautifulSoup(requests.get(url).content, "html.parser")

all_address = zillowSoup.find_all("address")
all_price = zillowSoup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
all_links = zillowSoup.find_all(class_="StyledPropertyCardDataArea-anchor")
allAddressList = []
allPriceList = []
allLinkList = []

for i in range(len(all_address)):
    print(f"Address: {all_address[i].get_text(strip=True)}")
    allAddressList.append(all_address[i].get_text(strip=True))

    price = re.sub(r"[^0-9$]", "", all_price[i].get_text(strip=True))
    allPriceList.append(price)
    print(f"Price: {price}")
    print(f"Link: {all_links[i].get('href')}")
    allLinkList.append(all_links[i].get('href'))
    print(i)
    i+=1
    print(f"------xxx--------")

print(allAddressList)
print(allPriceList)
print(allLinkList)


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option(name="detach",value=True)
driver = webdriver.Chrome(options=chromeOptions)

addressInput = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
priceInput = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
linkInput = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submitLink= '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

for j in range(len(allAddressList)):
    driver.get(googleFormUrl)
    time.sleep(3)

    input_fields = driver.find_element(By.XPATH, addressInput)
    input_fields2 = driver.find_element(By.XPATH, priceInput)
    input_fields3 = driver.find_element(By.XPATH, linkInput)
    enterSubmit = driver.find_element(By.XPATH, submitLink)

    print(f"-----------------------------")
    print(f"Current Number: {j}")
    input_fields.send_keys(allAddressList[j])
    input_fields2.send_keys(allPriceList[j])
    input_fields3.send_keys(allLinkList[j])
    enterSubmit.click()
    time.sleep(2)
    print(f"-----------------------------")





