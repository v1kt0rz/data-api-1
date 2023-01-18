import requests
BASE_URI = "https://weather.lewagon.com"

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
    print(forecast)
    print(len(forecast))
    for el in forecast:
        print(el["dt_txt"][0:10])
    return forecast




lat = 50.3494152
lon = -4.7050945

weather_forecast(lat, lon)
