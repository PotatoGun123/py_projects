import requests
from bs4 import BeautifulSoup as bs
import re
import smtplib
import time

url = "https://www.amazon.co.uk/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5NHG4H/ref=sr_1_3?dchild=1&keywords=m1%2Bmacbook%2Bair&qid=1618663448&sr=8-3&th=1"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
           }


def check_price():
    page = requests.get(url, headers=headers)

    soup = bs(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    price_float = float(re.search("^£(\d+.\d+)$", price).group(1))

    if price_float < 900:
        send_email()
    # print(price_float)
    # print(type(price_float))


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('tanikbhole@gmail.com', 'gjuevsnkwfextiri')

    subject = 'Price fell down for the M1 Macbook Air'

    body = f'Check this link ' + url

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'tanikbhole@gmail.com',
        'prashant_upadhyay101@hotmail.com',
        msg)

    print('Hey, the Email has been sent')
    server.quit()


check_price()

# while True:
#     check_price()
#     time.sleep(24 * 60 * 60)
