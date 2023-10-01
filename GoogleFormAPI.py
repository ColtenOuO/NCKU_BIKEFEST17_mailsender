import pygsheets
import json
with open('token.json') as f:
    token = json.load(f)

gc = pygsheets.authorize(service_file = token["service_file"])
sht = gc.open_by_url(token["url"])

def get_form_data(Data) -> list:
    wks_list = sht.worksheets() # list of sheets 
    sheets = wks_list[0]
    
    column_email = sheets.get_col(2)
    column_name = sheets.get_col(3)
    column_department = sheets.get_col(4)

    for i in range(3,500,1):
        if( column_email[i] == "" ): break

        student = [ column_email[i],column_name[i],column_department[i] ]
        Data.append(student)
    
    return Data

def get_department() -> list:
    wks_list = sht.worksheets()
    sheets = wks_list[0]

    column_department1 = sheets.get_col(11)
    column_department2 = sheets.get_col(12)
    column_department3 = sheets.get_col(13)

    return [ column_department1 , column_department2 , column_department3 ]

    