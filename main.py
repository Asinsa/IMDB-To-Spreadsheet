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

# Fetch everything in the google sheet
sheet = client.open("Films, TV Shows and Books").sheet1

#Print everything in the google sheet
#python_sheet = sheet.get_all_records()
#pp.pprint(python_sheet)

# OMDB Api Key
file = open("api_keys/apiKey.txt", 'r')
apiKey = file.readline(20)

# Fetch Movie Data from OMDB
def getData(movieTitle, yearOfRelease):
    data_URL = 'http://www.omdbapi.com/?apikey=' + apiKey
    year = yearOfRelease
    movie = movieTitle
    params = {
        't': movie,
        'type': 'movie',
        'y': year
    }
    response = requests.get(data_URL, params=params).json()
    #pp.pprint(response)
    if response != {'Response': 'False', 'Error': 'Movie not found!'}:
        information = [response['Director'], response['Genre'], response['Country'], response['Language'], response['imdbRating'], '=IMAGE("' + response['Poster'] + '")']
        return information

def update(row, info):
    # Update Cell
    column = 4
    for columnInfo in info:
        cell = sheet.cell(row, column)
        if cell.value != "":
            sheet.update_cell(row, column, columnInfo)
            column = column + 1

#Fetch column
nameCol = sheet.col_values(1)
yearCol = sheet.col_values(2)
for i in range(len(nameCol)):
    if len(nameCol[i]) > 1 and nameCol[i] != "11. Film":
        if "-" in nameCol[i]:
            nameCol[i] = nameCol[i].split('-')[1].lstrip().split(' ')[0]
            update(i, getData(nameCol[i], yearCol[i]))