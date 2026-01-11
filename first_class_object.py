# First Class Objects

# Store it in variables - Can be assign to any variable
# Pass it as a function argument - Argument  of the function
# Return it from a function- 
# Store it in data structures (lists, tuples, dicts)
# Create them at runtime

# list is first class object

lst=[10, 20, 30, 40, 55, 60]

# 1 List can be Assign to the variable
lst1=lst # 
print(lst1)

# 2 list can be passed as an argument to the function
def list_count_element(lst):
    no_elements=len(lst)
    print(no_elements)

list_count_element([10, 20, 30, 40, 50, 60])

# 3 list can be return from the function
def list_elements(len_lst):
    return list(range(len_lst))
    
length_of_list=int(input("Enter your length"))
print(list_elements(length_of_list))

# Store in data structure like tuple

tupp=(89, 20, 30, lst)
lst2=[10, lst]
print(tupp)

#--------------------------------------------------------------------------------------------------------------------------#


# function is a first class object

#1 function can be assign to any variable

def list_sqr(length_of_list):
    print(length_of_list*2)

sqr_list=list_sqr
print(sqr_list(length_of_list))

# Function can be passed as an argument to the function

def outer(fun_s): # 1st function
    print(fun_s())

def sqr_number(): # 2nd function
    return 5**2
outer(sqr_number) # passing 2nd function as an argument to the first function

# function can be returned from the function

def outer():
    def inner():
        print("Inside inner")
    return inner

inner=outer()
inner()

# function can be stored in data structure
lst=[outer(), sqr_number, sqr_list]
print(lst)
