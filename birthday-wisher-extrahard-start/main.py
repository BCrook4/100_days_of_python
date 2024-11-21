##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import smtplib
import pandas

EMAIL = "bcrookprog@gmail.com"
PASSWORD = "phatemtrjrpiozqk"
PLACEHOLDER = "[NAME]"
today = (dt.datetime.today().month, dt.datetime.today().day)
# print(today)


data = pandas.read_csv("birthdays.csv")
# print(data)

bday_dict = {(row.month, row.day):row for (index, row) in data.iterrows()}

if today in bday_dict:
    name = bday_dict[today]["name"]

    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        body = letter_file.read()
        body = body.replace(PLACEHOLDER, name)
        body = body.replace("Angela", "Benton")
        # print(letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="bcrookprog@yahoo.com",
            msg="Subject:Happy Birthday!\n\n"
                f"{body}"
        )



