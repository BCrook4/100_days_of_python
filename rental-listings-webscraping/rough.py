from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup
import requests
# from dotenv import load_dotenv
import time



FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScyO8q9hxRpx5_OXMhtOQWCSFEoVYpYmneNWQio7duPj2aTHw/viewform?usp=sf_link"

practice_url = "https://appbrewery.github.io/Zillow-Clone/"
url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-123.05474318457031%2C%22east%22%3A-121.81191481542969%2C%22south%22%3A37.46419422792466%2C%22north%22%3A38.08508509077189%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}




def get_listings(site_url, browser_header):
    # use Beautiful soup to scrape website
    response = requests.get(url=site_url, headers=header)
    zillow = response.text
    soup = BeautifulSoup(zillow, features="html.parser")

    # get prices
    prices = [price.getText().split('+')[0].split('/')[0] for price in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
    # print(prices)

    # get link
    links = [link.get("href") for link in soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")]
    # print(links)

    # get address
    # might still need cleaned up
    addresses = [address.getText().split('|')[-1].strip() for address in soup.find_all(name="address")]
    # print(addresses)

    results = {
        "prices": prices,
        "links": links,
        "addresses": addresses
    }

    return results

def fill_form(address, price, link):
    # keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url=FORM_LINK)

    for i in range(0, len(price)):

        time.sleep(1)

        address_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_form.send_keys(address[i])

        price_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_form.send_keys(price[i])

        link_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_form.send_keys(link[i])

        submit = driver.find_element(By.CLASS_NAME, value="NPEfkd.RveJvd.snByac")
        submit.click()

        time.sleep(1)

        another = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        another.click()

    driver.close()


listings = get_listings(practice_url, header)

fill_form(address=listings['addresses'],
          price=listings['prices'],
          link=listings['links'])

