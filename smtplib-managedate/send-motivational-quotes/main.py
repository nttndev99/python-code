import smtplib
import datetime as dt
import random

MY_EMAIL = "nttndev99@gmail.com"
MY_PASSWORD = "iohqiqvqrgrrtyug"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("./smtplib-managedate/send-motivational-quotes/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )