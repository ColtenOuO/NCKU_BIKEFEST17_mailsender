from DB import query_email
from GoogleFormAPI import get_form_data
from typing import List
from sendmail import send_mail
from counting import counting

class FormData:
    def __init__(self,Data: list) -> None:
        self.ALL_Data = Data    

class UserData:
    def __init__(self,email: str,name: str,department: str) -> None:
        self.department = department
        self.name = name
        self.email = email
    
Pre_Data: list = FormData(get_form_data([]))


for i in range(len(Pre_Data.ALL_Data)):
    student = UserData(Pre_Data.ALL_Data[i][0],Pre_Data.ALL_Data[i][1],Pre_Data.ALL_Data[i][2])
    #already = query_email(student)
    #if( already == False ): send_mail(student.email)

counting()