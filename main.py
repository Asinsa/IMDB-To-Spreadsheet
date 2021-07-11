import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from pprint import PrettyPrinter

pp = PrettyPrinter()

# Authorize the google sheets API
scope = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file"
    ]

file_name = "api_keys/client_key.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
client = gspread.authorize(creds)

# Fetch & print everything in the google sheet
sheet = client.open("Films, TV Shows and Books").sheet1
python_sheet = sheet.get_all_records()
pp.pprint(python_sheet)

# OMDB Api Key
file = open("api_keys/apiKey.txt", 'r')
apiKey = file.readline(20)

# Fetch Movie Data from OMDB
data_URL = "http://www.omdbapi.com/?apikey=" + apiKey
year = ""
movieTitle = "Fast & Furious"
params = {
    's':movieTitle,
    'type':'movie',
    'y':year
}

response = requests.get(data_URL,params=params).json()
pp.pprint(response)