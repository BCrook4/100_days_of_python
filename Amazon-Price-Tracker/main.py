import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import smtplib

load_dotenv(".env.txt")
MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")

practice_url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.ca/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Firefox User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0
# Header
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

response = requests.get(url=url, headers= header)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, features="html.parser")

# Find the HTML element that contains the price
# Remove the dollar sign using split
# Convert to floating point number
price = float(soup.find(name= "span", class_="aok-offscreen").getText().split('$')[1])

# get product name
product_name = soup.find(name="span", id="productTitle").getText().split()
product_name = ' '.join(product_name)#.encode('utf-8')

# test to check name and price
# print(product_name)
# print(price)

# send email if price passes low price check
if price < 140.00:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="bcrookprog@gmail.com",
            msg="Subject: Low Price Alert!\n\n"
                f"Low Price on '{product_name}'.\nNow only ${price}!\n{url}".encode("utf-8")
        )