
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS_ADMIN = "nttndev99@gmail.com"
EMAIL_PASSWORD_ADMIN = "iohqiqvqrgrrtyug"

#----- Send email -----#
def send_email(name, email, phone, message):
    msg = f"Subject:Contact Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS_ADMIN, EMAIL_PASSWORD_ADMIN)
        connection.sendmail(EMAIL_ADDRESS_ADMIN, EMAIL_ADDRESS_ADMIN, msg)


