import requests

city = input('City name = ')

print(f"Displaying the weather report of {city}:")

url = f'https://wttr.in/{city}'
res = requests.get(url)

print(res.text)
