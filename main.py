from decimal import Decimal

import requests
from bs4 import BeautifulSoup

url = 'https://www.finmarket.ru/currency/rates/?id=10123'

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find('div', class_='value')

usd = Decimal(data.text.replace(',', '.'))
try:
    money_usd = int(input("Введите сумму в долларах: "))
except ValueError:
    print("Некорректное значение")
    raise ValueError("Некорректное значение")
money_kzt = money_usd * usd
print(f"Сумма в тенге: {money_kzt}")
