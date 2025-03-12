import csv

with open('profiles1.csv', 'w',  newline='') as file:
    # cvs writer object by calling writter function
    writer = csv.writer(file, delimiter=" ") # if delimeter is not provided its {,} bydefault
    field = ["name", "age", "country"]

    # Storing data to csv file
    writer.writerow(field)
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])# used to store single row in csv file
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "United Kingdom"])
    writer.writerows([["Vini", 30], ["Rian", 60]]) # storing multiple row in file

mydict =[{'name': 'Kelvin Gates', 'age': '19', 'country': 'USA'}, 
         {'name': 'Blessing Iroko', 'age': '25', 'country': 'Nigeria'}, 
         {'name': 'Idong Essien', 'age': '42', 'country': 'Ghana'}]

fields = ['name', 'age', 'country'] 

with open('profiles2.csv', 'w', newline='') as file: 
    # csv.DictWriter object by calling DictWriter function
    writer = csv.DictWriter(file, fieldnames = fields, delimiter=" ")

    # Storing data to csv file
    writer.writeheader()
    writer.writerows(mydict) # multiple data at a time
    # writer.writerow({'name':"Veer", "age":50, "Country":'India'}) # Error - dict contains fields not in fieldnames: 'Country'
    writer.writerow({'name':"Veer", "age":50, "country":'India'})

# Reading data from the csv file
with open("profiles1.csv", 'r') as r_file:
    reader=csv.reader(r_file)
    print(reader)
    for lines in reader:
        print(lines)

with open("profiles2.csv", 'r') as rd_file:
    dict_reader=csv.DictReader(rd_file)
    print(rd_file)
    for d_lines in dict_reader:
        print(d_lines)


