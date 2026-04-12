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
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

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

        print("EMAIL_ADDRESS =", EMAIL_ADDRESS)
        print("user_email =", user_email)
        print("message =", message)

        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            return "❌ EMAIL_ADDRESS 或 EMAIL_PASSWORD 沒有設定"

        if not user_email or not message:
            return "❌ Email 或訊息不能空白"

        msg = MIMEText(
            f"Sender: {user_email}\n\nMessage:\n{message}",
            "plain",
            "utf-8"
        )
        msg["Subject"] = "New message from website"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Reply-To"] = user_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            return "✅ Email sent successfully!"
        except Exception as e:
            print("SEND ERROR:", e)
            return f"❌ Failed to send email: {e}"

    return render_template("contact.html")


if __name__ == "__main__":
    app.run()

#上傳 #git add .
# #git commit -m"update project"
# #git push
