from bs4 import BeautifulSoup
import requests
import time
import random as ran
import sys
import requests
import random



url = 'https://www.mudah.my/penang/cars-for-sale'

source = requests.get(url).text

requests.get(url).status_code

soup = BeautifulSoup(source, 'html.parser')

data_blocks = []
data_blocks = soup.find_all('div',{'class':'sc-fYiAbW htSrAb'})

print(len(data_blocks))

try:
    name = data_blocks[0].find('a').get_text()
    print('Car Name :', name)
except:
    pass

try:
    price = data_blocks[0].find('div',{'class':'sc-eilVRo kpBaOf'}).get_text()
    print('Price :', price)
except:
    pass

try:
    condition = data_blocks[0].find('div',{'title':'Condition'}).get_text()
    print('Concdition :', condition)
except:
    pass

try:
    mileage = data_blocks[0].find('div',{'title':'Mileage'}).get_text()
    print('Mileage :', mileage)
except:
    pass

try:
    manufactured_year = data_blocks[0].find('div',{'title':'Manufactured Year'}).get_text()
    print('Manufactured Year :', manufactured_year)
except:
    pass

try:
    engine_capacity = data_blocks[0].find('div',{'title':'Engine capacity'}).get_text()
    print('Engine capacity :', engine_capacity)
except:
    pass
