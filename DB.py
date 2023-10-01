from pymongo import MongoClient
import json

with open('token.json') as f:
    token = json.load(f)

client = MongoClient(token["db_client"])
db = client.Form_Data

def query_email(student) -> bool:
    
    Find: bool = False
    
    for i in db["User_Data"].find():
        if( student.email == i["email"] ):
            Find = True
            break
    
    if( Find == True ): return True
    else:
        # Adding to DataBase
        Adding_data = {
            "department": student.department,
            "name": student.name,
            "email": student.email
        }

        db["User_Data"].insert_one(Adding_data)

        return False