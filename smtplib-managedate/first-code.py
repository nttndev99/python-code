# import smtplib
import  datetime as dt

# ------------------------------------ First smtplib
# my_email = "nttndev99@gmail.com"
# password = "iohqiqvqrgrrtyug"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="nttn.doc@gmail.com", 
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()

# ------------------------------------ First datetime
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)