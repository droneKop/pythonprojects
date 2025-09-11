from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import  time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://ozh.github.io/cookieclicker/"
driver.get(url=url)
click_cookie = driver.find_element(By.ID, value="bigCookie")

i = 0
grandmaCount=0
totalGrandmaPrice = 0
grandmaLink = '//*[@id="product1"]/div[3]'

framCount = 0
factoryCount = 0
mineCount = 0
shipmentCount = 0
alchemyCount = 0
portalCount = 0
cookieCount =0


print("Starting while loop!")
while i<1000:
    click_cookie.click()
    i+=1
    grandmaPrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[2]/div[3]/span").text.replace(",",""))
    farmPrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[3]/div[3]/span").text.replace(",",""))
    factoryPrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[4]/div[3]/span").text.replace(",",""))
    minePrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[5]/div[3]/span").text.replace(",",""))
    shipmentPrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[6]/div[3]/span").text.replace(",",""))
    alchemyPrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[7]/div[3]/span").text.replace(",",""))
    portalPrice = float(driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[8]/div[3]/span").text.replace(",",""))
    # time.sleep(1)
    cookieCount = float(driver.find_element(By.ID, value="cookies").text.split(" ")[0].replace(",",""))
    # print("----xxx------")

    if cookieCount > grandmaPrice and grandmaCount<=5:
        grandmaCount += 1
        print("Buying Grandma!!")
        totalGrandmaPrice+=grandmaPrice
        print(f"Purchased so far:{totalGrandmaPrice}")
        portalClick = driver.find_element(By.XPATH, value=grandmaLink)
        # print("element found")
        portalClick.click()
        # print("yay Grandma")
        print(f"new grandma count: {grandmaCount}")
        time.sleep(0.5)
    else:
        pass


    # tMachinePrice = driver.find_element(By.XPATH, value="")
    # antimatterPrice = driver.find_element(By.XPATH,
    #                                     value="")
    # prismPrice = driver.find_element(By.XPATH,
    #                                       value="")
    # if cookieCount > portalPrice:


# time.sleep(2)
# print(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
# print(cookieCount)
# print("------")
# print(f"GrandmaPrice: {driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[12]/div[1]/div[3]/div[2]/div[3]/span").text}")
# print("########")
# print(f"Farm Price: {float(farmPrice.text.replace(","  ""))}")
# print(f"Factory Price: {float(factoryPrice.text.replace("," ,""))}")
# print("------")
# print(f"Mine Price: {minePrice.text.replace(",","")}")
# print("########")
# print(f"shipmentPrice: {shipmentPrice.text.replace(",","")}")
# print("------")
# print(f"alchemyPrice: {alchemyPrice.text.replace(",","")}")
# print("########")
# print(f"portalPrice: {portalPrice.text}")
# print("------")
# print(f"cookieCount: {cookieCount}")
# print("########")
# print(type(float(farmPrice.text.replace(",",""))))
# print("------")
# print(type(factoryPrice.text.replace(",","")))
# print("########")
# print(type(minePrice.text))
time.sleep(100)
driver.close()
driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys
#
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=chrome_options) # creating the object
#
# # driver.get("https://gem.gov.in/")
# # driver.get("https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2?ref_=ast_sto_dp")
# # driver.get("https://www.python.org/")
# # driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.get("https://secure-retreat-92358.herokuapp.com/")
#
#
# # # ------For url number 5 above - Form update------
# fNameTag = driver.find_element(By.NAME, value="fName")
# lNameTag = driver.find_element(By.NAME, value="lName")
# emailTag = driver.find_element(By.NAME, value="email")
#
# fNameTag.send_keys("Utsav")
# lNameTag.send_keys("Hansaria")
# emailTag.send_keys("jhingalala@ho.ho")
# emailTag.send_keys(Keys.ENTER)
#
#
#

# # ------For url number 4 above - Wikipedia------
# searchBar = driver.find_element(By.NAME, value="search")
# print("-----")
# searchBar.send_keys("Doland Trump")
# print("-----")
# searchBar.send_keys(Keys.ENTER)
# nameTag = driver.find_element(By.LINK_TEXT, value="Harry Crerar")
# print(nameTag.text)
# nameTag.click()
# burialPlace = driver.find_element(By.LINK_TEXT, value="Beechwood Cemetery")
# print(burialPlace.text)
# burialPlace.click()



# # ------For url number 4 above - Wikipedia------
# english_article_count = driver.find_element(By.XPATH,value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[2]/a[1]")
# print(english_article_count.text)
# ------------------------------------------------------------------------




# ------For url number 3 above - Python Website------
# upcomingEventDates = driver.find_elements(By.CSS_SELECTOR, value="ul li time")
# upcomingEventDesc = driver.find_elements(By.CSS_SELECTOR, value="section div div div ul li a")
# # for item in upcomingEventDates:
# #     print(item.text)
# #
# # for item in upcomingEventDesc:
# #     print(item.text)
# event_dict = {}
# for i in range(5,len(upcomingEventDates)):
#     dict_item = {"date":upcomingEventDates[i].text,
#                      "event":upcomingEventDesc[i].text
#                      }
#     event_dict[str(i-5)] = dict_item
# print(event_dict)
# ------------------------------------------------------------------------



# ------For url number 2 above - Amazon Product link------
# price_rs = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"The price is: {price_rs.text}")
# seller_from_css = driver.find_element(By.ID, value="sellerProfileTriggerId")
# print(f"The Seller is: {seller_from_css.text}")
# delivery_xpath1 = driver.find_element(By.XPATH, value='//*[@id="contextualIngressPtLabel_deliveryShortLine"]')
# delivery_xpath2 = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[5]/div[1]/div[3]/div/div/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[4]/div[10]/div[2]/span/a/div/div/div/span/div")
# print("------")
# print(f"Delivery Location 1: {delivery_xpath1.text}")
# print(f"Delivery Location 2: {delivery_xpath2.text}")
# print(f"Delivery Location 2: {delivery_xpath2.get_attribute("id")}")
# # driver.close()
# # driver.quit()
# ------------------------------------------------------------------------




