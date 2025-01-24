# Dictionary of List

# Employee Record Program

# emp={
#     'name':[],
#     'loc': [],
#     'sal':[]
# }

# no_record=int(input("How many record u want to store"))
# while(no_record>0):
#     e_name=input("Enter emp name:")
#     e_loc=input("Enter emp location:")
#     e_sal=input("Enter emp salary")
#     emp['name'].append(e_name)
#     emp['loc'].append(e_loc)
#     emp['sal'].append(e_sal)
#     no_record=no_record-1

# # Display all records
# print("Employee Records", emp) 

# # Display Record by record
# for e_name, e_loc, e_sal in zip(emp['name'], emp['loc'], emp['sal']):
#     print(e_name, "-", e_loc, "-", e_sal)
# # 2nd way
# rec=0
# for record in zip(emp['name'], emp['loc'], emp['sal']):
#     rec=rec+1
#     print(f"Record {rec} - {record}")

# # Get the name from the user and fetch the data of that user from the record
# while True:
#     e_name=input("Please enter user name:")
#     if not e_name: # len(e_name)==0
#         break
#     if e_name in emp['name']:
#        id_r=emp['name'].index(e_name) # index position of name
#        print(id_r)
#        # Retreiving location and salary of the employee
#        e_loc=emp['loc'][id_r]
#        e_sal=emp['sal'][id_r]
#        print(f"{e_name} is located in {e_loc} and, has {e_sal}")
#     else:
#         print("Name doesn't exist in record")
    
# -----------------------------------------------------------------------------------------------------------------------------------------------   

# Dictionary of dictionary

# Creating and storing data in nested dictionary

# emp={
# '1': {
# 'name': 'tera', 
# 'loc': 'Gondia'
#},
#}

# empty Dictionary
emp={}
for i in range(1, 2):
    eid=input("Please enter your id")
    ename=input("Please enter your name")
    eloc=input("Please enter your location")
    emp[eid]={} # This is empty

    # Adding data to eid
    emp[eid]['name']=ename
    emp[eid].update(loc="Gondia") # Adding data by using keyword argument
print(emp)

# Accessing all data & display it
for key, value in emp.items():
    # print(key, '-', value )
    print("e_id", '-', key, '-', "Name", '-', value['name'], '-', "Location", '-', value['loc'])
print(list(emp.items())) # [('1', {'name': 'poorav', 'loc': 'Gondia'})]

# Retreive the value from dictionary by eid
while True:
    eid=input("Please enter your eid")
    if not eid:
        break # if user doesn't enter anything
    # Checking emp id is exist in emp record
    if eid in emp:
        ename=emp[eid]['name']
        eloc=emp[eid]['loc']
        print(f"Eid {eid} name is {ename} and located in {eloc}")
    else:
        print("Employee id doesn't exit in record")





