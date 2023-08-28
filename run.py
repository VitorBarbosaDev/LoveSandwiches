# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import gspread
from google.oauth2.service_account import Credentials

# Define the scope for Google APIs
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the service account file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize and connect to Google Sheets
GSPREAD = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet
SHEET = GSPREAD.open('love_sandwiches')


# Access the 'Sales' worksheet
sales = SHEET.worksheet('sales')

# Retrieve all values from the 'Sales' worksheet
data = sales.get_all_values()

# Print the data
print(data)




