import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-googlesheets-205d269aacf3.json', scope)

gc = gspread.authorize(credentials)

spreadsheet = gc.open('python-automation').sheet1

worksheet = spreadsheet.duplicate(new_sheet_name='copied2')
