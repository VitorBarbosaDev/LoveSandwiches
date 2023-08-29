# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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

def get_sales_data():
    ''''
    Get the sales data from the user
    '''
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers separated by a comma.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        if validate_sales_data(sales_data):
            print("Data is valid!\n")
            break
    return sales_data


def validate_sales_data(values):
    """
    Validate the sales data
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 numbers should be entered, but {len(values)} were entered."
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet_name):
    """
      Receives a list of integers to be inserted into a worksheet.
      Updates the relevant worksheet data in the worksheet.
      """
    print(f"Updating {worksheet_name} data...\n")
    sales_worksheet = SHEET.worksheet(worksheet_name)
    sales_worksheet.append_row(data)
    print(f"{worksheet_name} data updated Successfully!\n")



def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock :
    - Postive surplus indicates waste
    - Negative surplus indicates extra made when stock ran out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data





def main():
    """
    Run all the functions
    """
    data = get_sales_data()

    sales_data = [int(num) for num in data]

    update_worksheet(sales_data, "sales")

    new_surplus_data = calculate_surplus_data(sales_data)

    update_worksheet(new_surplus_data, "surplus")


print("Welcome to the Love Sandwiches Data Automation Tool!\n")
main()
