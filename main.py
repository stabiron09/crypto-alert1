import requests
import sys
import urllib3
import re
import smtplib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
y="https://www.indiainfoline.com/top-share-market-news/1"
url= y
x=requests.get(url, verify=False)
z=x.text
x=(re.search('Top 10 stocks for today', z, re.IGNORECASE))
if x:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('keerak0009@gmail.com', 'oywqosuhvhqxtlvy')
    server.sendmail('keerak0009@gmail.com', 'arpitkeer11@gmail.com', 'bhai indiainfolline pe update as chuke hai <a href="https://www.indiainfoline.com/top-share-market-news/1">click me</a>')
else:
    print("sorry")
