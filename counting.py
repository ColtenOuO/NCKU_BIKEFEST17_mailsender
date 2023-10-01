from GoogleFormAPI import get_department

class NCKU_Bike:
    def __init__(self) -> None:
        self.N1 = 0
        self.N2 = 0
        self.N3 = 0

all = [ "策展部" , "學術部" , "行銷部" , "公關部" , "影紀部" , "設計部" , "秘書部" ]

def counting() -> None:
    
    NCKU_Bike_Department = { 
    "秘書部": NCKU_Bike(),
    "公關部": NCKU_Bike(),
    "行銷部": NCKU_Bike(),
    "設計部": NCKU_Bike(),
    "策展部": NCKU_Bike(),
    "學術部": NCKU_Bike(),
    "影紀部": NCKU_Bike()                    
                         }

    department_choise = get_department()
    for i in range(3):
        for k in department_choise[i]:
            for s in all:
                if( k == s ):
                    if( i == 0 ): NCKU_Bike_Department[s].N1 += 1
                    if( i == 1 ): NCKU_Bike_Department[s].N2 += 1
                    if( i == 2 ): NCKU_Bike_Department[s].N3 += 1

    for i in all:
        print(i,f"第一志願：{NCKU_Bike_Department[i].N1}")
        print(i,f"第二志願：{NCKU_Bike_Department[i].N2}")
        print(i,f"第三志願：{NCKU_Bike_Department[i].N3}")
        print("-------------------------------------------")