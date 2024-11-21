from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# the '#' denotes html ID while '.' denotes class
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# article_count.click()

# click_x = driver.find_element(By.CSS_SELECTOR, value=".frb-form-wrapper button")
# click_x.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()


open_search = driver.find_element(By.CLASS_NAME, value="vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
open_search.click()

time.sleep(2)

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()