from datetime import date
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('xr-club-checking-691d825c8eb1.json', scope)
client = gspread.authorize(creds)

sheet = client.open("XR Club checkin'").worksheet("checkin' data")

sheet.update_cell(1, 1, "ID_Number")
sheet.update_cell(1, 2, "Time")
sheet.update_cell(1, 3, "Date")
sheet.update_cell(1, 4, "MATA_DATA")
i = sheet.cell(9, 9).value

while True:
    i_int = int(i)
    i_int = i_int + 1
    val = input("id")
    print(type(val))
    if len(val) > 10:
        value = ''
        for word in val:
            if word.isdigit():
                value = value + word
        string = "=MATCH(" + value + ",A2:A" + i + ",0)"
        sheet.update_cell(i_int, 4, string)
        if sheet
        sheet.update_cell(i_int, 1, value)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        today = str(today)

        sheet.update_cell(i_int, 2, current_time)
        sheet.update_cell(i_int, 3, today)
        i = str(i_int)
        sheet.update_cell(9, 9, i)
    else:
        print("Swipe Again !!")
