from bs4 import BeautifulSoup
import requests
import time
import random as ran
import sys
import requests

url = 'https://www.mudah.my/malaysia/properties-for-sale'

source = requests.get(url).text


requests.get(url).status_code

soup = BeautifulSoup(source, 'html.parser')

data_blocks = []
data_blocks = soup.find_all('div',{'class':'sc-fYiAbW htSrAb'})

print(len(data_blocks))

try:
    name = data_blocks[0].find('a').get_text()
    print('House Name :', name)
except:
    pass

try:
    price = data_blocks[0].find('div',{'class':'sc-eilVRo kpBaOf'}).get_text()
    print('Price :', price)
except:
    pass

try:
    category = data_blocks[0].find('div',{'title':'Category'}).get_text()
    print('Category :', category)
except:
    pass

try:
    size = data_blocks[0].find('div',{'title':'Size'}).get_text()
    print('Size :', size)
except:
    pass

try:
    titletype = data_blocks[0].find('div',{'title':'Title type'}).get_text()
    print('Land Title :', titletype)
except:
    pass

try:
    propertytype = data_blocks[0].find('div',{'title':'Property type'}).get_text()
    print('Type :', propertytype)
except:
    pass

try:
    bedrooms = data_blocks[0].find('div',{'title':'Bedrooms'}).get_text()
    print('Bedroomns :', bedrooms)
except:
    pass

try:
    bathrooms = data_blocks[0].find('div',{'title':'Bathrooms'}).get_text()
    print('Bathrooms:', bathrooms)
except:
    pass