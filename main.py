import requests
from bs4 import BeautifulSoup
import smtplib

amazon_url="https://www.amazon.ae/Tefal-Oilless-Capacity-EY201827-warranty/dp/B07RXCZFPF/ref=sr_1_2_sspa?keywords=instant%2Bpot%2Bair%2Bfryer&qid=1670501128&sprefix=instant%2Bpot%2Caps%2C175&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
headers={"accept_language"
:"en-US,en;q=0.9",
"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
response=requests.get(url=amazon_url,headers=headers)
webpage=response.text

soup=BeautifulSoup(webpage,"html.parser")
price=soup.find(class_="a-price-whole").get_text().split(".")[0]
price_with_float=float(price)
product_title=soup.find(id="productTitle").get_text()
print(product_title)
buy_price=300

my_email="newtester420@gmail.com"
my_password= "qwnjfytbgjevradi"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if price_with_float < buy_price:
       connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"subject:amazon price alert!\n\n{product_title}\n{price}\n{amazon_url}")