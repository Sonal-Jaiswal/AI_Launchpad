
request = int(input("number of total request"))

AList = []

for i in range(request):
    citizen_name=input("Name:")
    Aadhaar_Service_Type=input("Service type")
    Citizen_Age=int(input("Age"))
    Service_Fee=int(input("numb"))


    # Citizen age must be greater than zero.
    if not Citizen_Age>0:
        print("age greater than zero")
        
    # Service fee must be zero or greater.
    if not Service_Fee >=0:
        print("fee should be equal or greater than zero")
        
    list.append([citizen_name,Aadhaar_Service_Type,Citizen_Age,Service_Fee])



