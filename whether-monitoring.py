# Weather App (using API)

# Take a city name as input.

# Fetch real-time weather using [OpenWeatherMap API].

# Show temperature, humidity, and description.
# # (Concepts: requests, JSON, APIs)

import requests as rq
from bs4 import BeautifulSoup
url="https://w3schools.com"
x=rq.get(url)


print(x.status_code)
print(x.text)
print("_________________________________________")
#200 status code
y=rq.head(url)  
print(y.headers)
#resoponse
# response =rq.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# text = soup.get_text(separator="\n", strip=True)

# print(text)