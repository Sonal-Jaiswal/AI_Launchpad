emp_dataa = {
    '110' : ['Ritik', 25, 980000, 15000,'A']
} 
emp_data = {
    '110' :{
        'name' : 'Ritik',
        'age' :24,
        'gross-salary':980000,
        'bonus':49000,
        'grade':'A'
 
    },
    '111':{
        'name' : 'Sai Pallavi',
                'age' :22,
                'gross-salary':880000,
                'bonus':47000,
                'grade':'A'
    }
} 
print(emp_data['110'])
print(emp_data['110']['name'])
 
# dictionary methods
print(emp_data.keys()) # print all keys
print(emp_data.values()) # print all values
print(emp_data.items())
 