import requests
from bs4 import BeautifulSoup
import smtplib
import csv
import datetime
import os
import time

#def send_email():
    





url = "https://www.amazon.in/Samsung-Fully-Automatic-Loading-Washing-WW90T504DAN1TL/dp/B09T6XD839/ref=sr_1_1_sspa?pf_rd_i=1380369031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=9e52fb75-d512-4d6e-8d0c-3bca7e227c77&pf_rd_r=YN3D0RX82TMDGB1PGZ8V&pf_rd_s=merchandised-search-6&pf_rd_t=101&qid=1657458950&refinements=p_n_feature_fifteen_browse-bin%3A2753053031%2Cp_85%3A10440599031&rps=1&s=kitchen&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFFQ1FVVUNKUkUwSjUmZW5jcnlwdGVkSWQ9QTA3MDE5MTYxSjZRUTRRMkRUU1NJJmVuY3J5cHRlZEFkSWQ9QTA1Mjc1NDIzMlQ4WVA3NFI2RVpFJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

#def check_price():
page = requests.get(url, headers=headers)
bs = BeautifulSoup(page.content, 'html.parser')

#print(bs.prettify().encode("utf-8"))
product_title = bs.find(id = "productTitle").get_text()
print(product_title.strip())
product_price = bs.find(id = "corePriceDisplay_desktop_feature_div").get_text()

product_price = product_price[9:15]
print(product_price)
price_float = float(product_price.replace(",",""))
print(price_float)

file_exists = True

if not os.path.exists("./price.csv"):
        file_exists = False

with open("pri.csv","a") as file:
        writer = csv.writer(file,lineterminator ="\n")
        fields = ["Timestamp","price"]
        
        if not file_exists:
            writer.writerow(fields)

        timestamp = f"{datetime.datetime.date(datetime.datetime.now())},{datetime.datetime.time(datetime.datetime.now())}"
        writer.writerow([timestamp, price_float])
        print("wrote csv data")
#return price_float



while True:
    #price = check_price()
    if(price_float <= 320000):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('azimsohel267452@gmail.com', "mzutvnadyvzeumjo")

        subject= "Price decreased, Check new price"
        body = "Go and order now at sdf"
        msg = f"Subject:{subject}\n\n\n\n{body}"

        server.sendmail("azimsohel267452@gmail.com","azimsohel267452@gmail.com",msg)
        print("email sent")
        server.quit()
        #break
    time.sleep(20)