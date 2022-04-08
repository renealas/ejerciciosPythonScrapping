import requests
from bs4 import BeautifulSoup
import csv
from decimal import Decimal

query = input('Enter product: ')
free_shipping = input('Enter free shipping: ')
max_price = Decimal(input('Enter maximum price: '))

for i in range(1, 5):
    website = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + query + '&_pgn='+ str(i)).text
    soup = BeautifulSoup(website, 'html.parser')

    items = soup.select('.srp-results .s-item')
    for item in items:
        line = item.h3.text
        title = line.replace('Anuncio nuevo', '')
        lineprice = item.select_one('.s-item__price').text
        price = lineprice.replace('USD','$')
        lineshipping = item.select_one('.s-item__shipping').text
        shipping = lineshipping.replace('+USD', '+$')
        price_decimal = Decimal(lineprice.split(' a ')[0][3:])
        if price_decimal <= max_price:
            if free_shipping == 'y':
                if 'gratis' in lineshipping: 
                    print(f'{title} \n {price}\n{shipping}')
                    print('================================')
            else:
                print(f'{title} \n {price}\n{shipping}')
                print('================================')
        