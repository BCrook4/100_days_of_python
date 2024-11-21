from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get(url="http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Ben")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Crook")

email = driver.find_element(By.NAME, value="email")
email.send_keys("fakeemail@email.com")

button = driver.find_element(By.CLASS_NAME, value="btn.btn-lg.btn-primary.btn-block")
button.click()