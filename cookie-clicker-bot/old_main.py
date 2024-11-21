from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get(url="https://orteil.dashnet.org/cookieclicker/")
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

# get cookie button
cookie = driver.find_element(By.ID, value="cookie")

# get upgrade item IDs
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
del item_ids[-1]

# set 5s timer
timer_done = time.time() + 10
timer_5_mins = time.time() + 5*60

while True:
    cookie.click()
    # check purchases every 5s
    if time.time() > timer_done:
        money = int(driver.find_element(By.ID, value="money").text)
        # get item buttons
        items = driver.find_elements(By.CSS_SELECTOR, value="#store div")

        #get item costs
        items_cost = [item.text.split("-")[-1].strip() for item in driver.find_elements(By.CSS_SELECTOR, value="#store b") if item.text != ""]
        # del items_cost[-1]
        items_cost = [int(item.replace(',', '')) for item in items_cost]

        # check for most expensive upgrade we can afford
        affordable_ids = []
        for i in range(len(items_cost)-1, -1, -1):
            if money > int(items_cost[i]):
                driver.find_element(By.ID, value= item_ids[i]).click()
                break


        timer_done = time.time() + 10

        if time.time() > timer_5_mins:
            cpm = driver.find_element(By.ID, value= "cps").text
            print(cpm)
            break



