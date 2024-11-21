from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = "bcrookprog@gmail.com"
TWITTER_PASSWORD = "Ihatethis3!"
# TW1TT3RB0T1


class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value=".start-button a").click()
        time.sleep(50)
        # self.driver.find_element(By.CSS_SELECTOR, value=".svg-icon use").click()
        self.down = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(url="https://x.com/?lang=en")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value='.css-175oi2r.r-2o02ov a').click()
        time.sleep(2)
        login = self.driver.find_element(By.CLASS_NAME, value='css-175oi2r.r-1roi411.r-z2wwpe.r-rs99b7.r-18u37iz')
        login.send_keys(TWITTER_EMAIL)
        login.send_keys(Keys.ENTER)

        time.sleep(10)
        password = self.driver.find_element(By.CLASS_NAME, value='.css-175oi2r.r-18u37iz.r-1pi2tsx.r-1wtj0ep.r-u8s1d.r-13qz1uu')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)



bot = InternetSpeedBot()
# bot.get_internet_speed()
bot.tweet_at_provider()