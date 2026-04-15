from flask import (
    Flask, render_template, redirect, request,
    flash, url_for, session, send_from_directory
)
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import time
import os


app = Flask(__name__)

#email設定
# ⚠️ 改成你的 Gmail
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("SENDGRID_API_KEY")

# 首頁
@app.route("/")
def root():
    return redirect(url_for("home"))

# API：取得專案
@app.route("/home")
def home():
   return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/Guitar")
def Guitar():
    return render_template("Guitar.html")

@app.route("/website")
def website():
    return render_template("website.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not EMAIL_ADDRESS or not SENDGRID_API_KEY:
            return "❌ EMAIL_ADDRESS or SENDGRID_API_KEY is missing"

        if not user_email or not message:
            return "❌ Email and message are required"

        email = Mail(
            from_email=EMAIL_ADDRESS,
            to_emails=EMAIL_ADDRESS,
            subject="New message from website",
            plain_text_content=f"Sender: {user_email}\n\nMessage:\n{message}"
        )
        email.reply_to = user_email

        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(email)
            return f"✅ Email sent successfully! Status: {response.status_code}"
        except Exception as e:
            print("SENDGRID ERROR:", str(e))
            return f"❌ Failed to send email: {e}"

    return render_template("contact.html")

@app.route("/send")
def send():
    return render_template("send.html")

if __name__ == "__main__":
    app.run()

#上傳 #git add .
# #git commit -m"update project"
# #git push
