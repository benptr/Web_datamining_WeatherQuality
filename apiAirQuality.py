import requests, json
import pandas as pd

def getAirQuality(city="paris"):
    try:
        url = requests.get("https://api.waqi.info/feed/{}/?token=49a66ce7af17ad7c0c0cb12b3a75cea9930f5634".format(city))
        airQualityData = json.loads(url.text)
    except:
        print("Invalid query, The city selected must not exist in the api Data Base")
    return airQualityData

def getWeather(city="Paris"):
    try:
        url = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=ecab1e85cf8afd4829a1ea59134e3cf5".format(city))
        airQualityData = json.loads(url.text)
    except:
        print("Invalid query, The city selected must not exist in the api Data Base")
    return airQualityData

def CountryData(country="France"):
    cities = pd.read_csv('https://pkgstore.datahub.io/core/world-cities/world-cities_csv/data/6cc66692f0e82b18216a48443b6b95da/world-cities_csv.csv')
    country_city = cities[cities['country']==country]['name']
    result = {}
    for elmt in country_city:
        result[elmt] = {"airQ":getAirQuality(elmt),"weather":getWeather(elmt)}
        print(result[elmt])
    return result
