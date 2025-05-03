import smtplib
from flask import Flask, render_template, request
import requests

from post import Post

# get data from the API
# https://api.npoint.io/488de86bd28e4f09b2fe
posts = requests.get("https://api.npoint.io/488de86bd28e4f09b2fe").json()
# create a class to represent a post
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

MY_EMAIL = "nttndev99@gmail.com"
MY_PASSWORD = "iohqiqvqrgrrtyug"

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return render_template("index.html", all_posts=post_objects)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(name, email, phone, message)
        # send email
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:   
        return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == '__main__':
    app.run(debug=True, port=5001) 
