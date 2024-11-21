import smtplib
import datetime as dt
import random

my_email = "bcrookprog@gmail.com"
password = "phatemtrjrpiozqk"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="bcrookprog@yahoo.com", msg="Subject:Hello\n\n"
#                                                                                  "This is the body of my email")
LAUREN = "lauren.robinson21@outlook.com"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1998, day=13, month=8)

with open(file="quotes.txt") as file:
    quotes = file.readlines()

if day_of_week == 0:
    quote_of_day = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=LAUREN,
                            msg="Subject:Monday Motivation\n\n" f"{quote_of_day}")
