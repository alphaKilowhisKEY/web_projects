'''
Amazon Price Tracker

This Python script tracks the price of an item on Amazon and notifies you via email if the price drops below a specified threshold.

Requirements:
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `sender` module (for sending email notifications)

Usage:
1. Set the `URL` variable to the Amazon product page URL you want to track.
2. Set the `PRICE_NEEDED` variable to the price threshold below which you want to be notified.
3. Set the SENDER_EMAIL, SENDER_PASSWORD and HEADERS.
4. Run the script using Python:
$ python3 main.py
  
5. If the current price of the item is lower than the specified threshold, you will receive an email notification.

'''

from bs4 import BeautifulSoup
import requests
import sender

URL = "https://www.amazon.com/Electric-Adjustable-Standing-Workstation-Control/dp/B0CTZH93Z4/ref=sr_1_1?crid=3GS4LRONG57ZC&dib=eyJ2IjoiMSJ9.585FwC2Hsxfu1QieF7ZUskEDe6tcRGFqiKj7cJkQ-0VScKFZGyo_GZoU0TTGr_p4c3dyJii49hTUZnoDGTOV9Awl-1SSItQSNNXFLiDX0GHALUrsTYd6ehjtmBhUIlSdy6CqtG8wzn2PRzk96GkWkoRE_DjgBT6d3Ku8Xm48AGj-EFTKOg8cNu5iAP0epj9Ot68h9wmipjEMFhpPSlLWYz1dpM5P-Vl1dz_i2okFz8pTmGkkfu5_lO2PSuRTTYcNASPw4e6EmHVXS6b5lT2T6vV5MECvbCj1O2WNHBcVlPU.yAduAfdW_j-tzQ502VQtZuv9irpn1JKFdByboge7H3I&dib_tag=se&keywords=adjustable%2Btable&qid=1715359995&sprefix=adjustable%2Btab%2Caps%2C219&sr=8-1&th=1"
PRICE_NEEDED = 3000

SENDER = "******"
SENDER_PASSWORD = "****"

subject = "Lower Price Right Now!"
body = "Price is lower now."
recipients = ["recipient@email.com"]

# To get this value got to: https://myhttpheader.com/
HEADERS = {
    "User-Agent":"YOUR_USER_AGENT",
    "Accept-Languag":"YOUR_ACCEPT_LANGUAGE"
}


response = requests.get(URL, headers=HEADERS)
price_of_item = None

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    item_data = soup.find(name="span", class_="a-offscreen")
    price_of_item = float(item_data.split("$")[1])
else:
    print(f"[-] Response error. Status code: {response.status_code}")  

try:
    if price_of_item < PRICE_NEEDED:
       sender.send_notification(subject, body, SENDER, recipients, SENDER_PASSWORD, URL)  
except:
    print("Cannot send the message.")