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




@app.route("/send")
def send():
    return render_template("send.html")

if __name__ == "__main__":
    app.run()


#上傳 #git add .
# #git commit -m"update project"
# #git push
