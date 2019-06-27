import requests
from bs4 import BeautifulSoup
import smtplib
import time
# py -m pip install bs4 requests

URL = 'https://www.amazon.com/Apple-MNYH2LL-MacBook-Processor-Version/dp/B072QGRJQ4/ref=sr_1_3?keywords=macbook&qid=1561661289&s=gateway&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if converted_price < 1000:
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your@gmail.com', 'google-app-password')

    subject = 'Price fell down!'
    body = 'Check the amazon link ' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('your@gmail.com', 'to@email.com', msg)
    print('Hey Email has been sent!')
    server.quit()


while True:
    check_price()
    time.sleep(3600)
