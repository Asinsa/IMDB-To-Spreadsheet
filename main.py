import requests
from pprint import PrettyPrinter

pp = PrettyPrinter()
file = open("api_keys/apiKey.txt", 'r')
apiKey = file.readline(20)

#Fetch Movie Data
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
movieTitle = 'Fast & Furious'
params = {
    's':movieTitle,
    'type':'movie',
    'y':year
}

response = requests.get(data_URL,params=params).json()
pp.pprint(response)