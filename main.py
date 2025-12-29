from urllib.parse import urlparse, urlencode
import urllib
import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


url = "http://facebaaakk.pagekite.me/"

def send_email(subject, message):
    # Email configuration
    sender_email = "keerak0009@gmail.com"
    sender_password = ""
    receiver_email = "arpitkeer30@gmail.com"

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Website is up and running (Status 200 OK)")
    else:
        error_message = f"Website is down! Status code: {response.status_code} .check manually. or wait for few minutes if you stop receving the email means everything is fine now. check the mobile status with webview app."
        print(error_message)
        send_email("Website Down", error_message)
except requests.exceptions.RequestException as e:
    error_message = f"Error while trying to access the website: {str(e)}. an error occured means the website gone down few minutes ago. potentialy means power supply is down. phone is dead. or internet connection was lost. check webview for more information about phone"
    print(error_message)
    send_email("Website Error", error_message)
except Exception as e:
    error_message = f"An unexpected error occurred: {str(e)}"
    print(error_message)
    send_email("Website Error", error_message)


