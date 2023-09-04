from bs4 import BeautifulSoup
import requests
import tkinter as tk
import sqlite3

conn = sqlite3.connect('weatherbook.db')
c = conn.cursor()

#c.execute('''DROP TABLE weather''')
#c.execute('''CREATE TABLE weather(place TEXT, temperature INTEGER, wind INTEGER, humidity REAL, dewpoint REAL, pressure REAL, precipitation REAL, visibility REAL, UVindex INTEGER)''')

def weatherdata(url):

    source = requests.get(url)

    soup = BeautifulSoup(source.text, "lxml")

    place = soup.find_all('span', class_ = "d-inline-block")
    temperature = soup.find('li', class_ = "fs-2").text
    details = soup.find_all('ul', class_= "list-unstyled lh-sm mb-0")
            
    #choose current whether condition and temperature details and split it out
    weather_details = details[1].text
    weather_details = weather_details.split()

    #break down the whether details for each condition
    wind_break = [*weather_details[2]]
    humidity_break = [*weather_details[3]]
    dewpoint_break = [*weather_details[4]]
    pressure_break = [*weather_details[5]]
    precipitation_break = [*weather_details[6]]
    visibility_break = [*weather_details[7]]

    #join back of the condition 
    wind_back = ''.join(wind_break[:-9])
    humidity_back = ''.join(humidity_break[:-9])
    dewpoint_back = ''.join(dewpoint_break[:-9])
    pressure_back = ''.join(pressure_break[:-14])
    precipitation_back = ''.join(precipitation_break[:-11])
    visibility_back = ''.join(visibility_break[:-2])

    #final condition
    place = place[1].text 
    temperature = temperature
    wind =  weather_details[1] + wind_back
    humidity =  humidity_back
    dewpoint = dewpoint_back
    pressure =  pressure_back
    precipitation =  precipitation_back
    visibility =  visibility_back
    UVindex =  weather_details[9]
    
    c.execute('''INSERT INTO weather VALUES(?,?,?,?,?,?,?,?,?)''',(place, temperature, wind, humidity, dewpoint, pressure, precipitation, visibility, UVindex))
    #print(place, temperature, wind, humidity, dewpoint, pressure, precipitation, visibility, UVindex)
    return
    

weatherdata("https://www.weather-atlas.com/en/malaysia/ipoh")

conn.commit()
print("complete")

#c.execute('''DELETE from weather ''')
c.execute('''SELECT * from weather''')
result = c.fetchall()
print(result)

conn.close()