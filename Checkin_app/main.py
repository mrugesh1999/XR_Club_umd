from datetime import date
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('xr-club-checking-691d825c8eb1.json', scope)
client = gspread.authorize(creds)

sheet = client.open("XR Club checkin'").worksheet("checkin' data")
done_sheet = client.open("XR Club checkin'").worksheet("complete trades")


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
        try:
            reference = int(sheet.cell(i_int, 4).value)
            flag = True
        except:
            flag = False
        if flag:
            print("Second time swipe")
            sheet.update_cell(reference+1, 1, '')
            now_out = datetime.now()
            current_time_out = now_out.strftime("%H:%M:%S")
            today_out = date.today()
            today_out = str(today_out)
            current_time_in = sheet.cell(reference+1, 2)
            print(current_time_in)
            current_time_in = str(current_time_in)
            print(current_time_in)
            today_in = sheet.cell(reference+1, 3)
            position = done_sheet.cell(9, 9).value
            print(type(position))
            position = int(position)
            today_in = str(today_in)

            # today_in = today_in[len(to)]
            done_sheet.update_cell(position, 1, value)
            done_sheet.update_cell(position, 2, current_time_in)
            done_sheet.update_cell(position, 3, current_time_out)
            done_sheet.update_cell(position, 4, today_in)
            done_sheet.update_cell(position, 5, today_out)
            sheet.update_cell(reference+1, 1, '')
            done_sheet.update_cell(9, 9, str(position+1))
            flag = False
            continue
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
