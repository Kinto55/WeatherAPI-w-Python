##weather.py

from sys import api_version

import requests

API_KEY = "8cf925b71amsh31ce8067b3e97c4p15f074jsn6bbb13e4951e" # Get your own API key at https://rapidapi.com/weatherbit/api/weatherbit-io1
url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"

querystring = {"units":"auto","lang":"en"}
headers = {
	"X-RapidAPI-Key": "8cf925b71amsh31ce8067b3e97c4p15f074jsn6bbb13e4951e",
	"X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
}
## the response is a json file
## json is a file format that is used to store data in a structured format
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

## this city variable is the one you need to change to get the weather for a different city
city = input( "Enter city name : ")

## this url is for getting the weather of the city
request_url = f"{BASE_URL}?appid={api_version}&q={city}"
response = requests.get(request_url)

if response == 200:
    ## if the response is 200, it means the city is found
    data = response.json()
    ## the data is in json format, so we need to convert it to a dictionary
    main = data['main']
    temp = main['temp']
    ## the temperature is in kelvin, so we need to convert it to celsius
    weather = data['weather']
    ## description is the weather condition
    description = weather[0]['description']
    ## print the weather
    print(f"Temperature: {temp}°C")
    ## print the description
    print(f"Weather: {description}")
else:

    print("Error in the HTTP request")  ## No newline at end of file
