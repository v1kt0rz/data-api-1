# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    #create url for search made from BASE_URI, the endpoint and the city name and the limit option
    endpoint = "/geo/1.0/"
    all_but_query = f"direct?q={query}&limit=5"
    #make big url
    url = BASE_URI + endpoint + all_but_query

    response = requests.get(url).json()

    if response[0]["name"] == query:
        return response[0]
    return None

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    #for now just print something so i know the flow is working
    #https://weather.lewagon.com/data/2.5/weather?lat=50.3494152&lon=-4.7050945&units=metric
    #build url
    endpoint = "/data/2.5/"
    all_but_latlon = f"forecast?lat={lat}&lon={lon}&units=metric"

    url = BASE_URI + endpoint + all_but_latlon

    response = requests.get(url).json()

    ### the structure is dict "list" within the first dict of the response containing 40 entries (24/3*5)
    #so entry 0,9,17,25,33 should be separate days
    #date is in variable dt-txt in list[i] dict so response[list][i][dt-txt]
    forecast = response["list"][slice(0,34,8)]
    return forecast



def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    if not city:
        query = input("City?\n")
    forecast = weather_forecast(city["lat"], city["lon"])
    print(f"Here's the weather in {city['name'].capitalize()}")
    for el in forecast:
        #extract all variables from forecast for the day
        day = el["dt_txt"][0:10]
        desc = el["weather"][0]["description"]
        temp = el["main"]["temp"]

        print(day + " " + str(desc).capitalize() + " " + str(temp).capitalize())
    #pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
