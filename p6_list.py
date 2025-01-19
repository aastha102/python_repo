# creating empty list
l=[] 
l=list()

l=list(range(1,10,2))# starts from 1 till 9 with incremented by 2
#range(start:end:steps)# l=[1,3, 5, 7, 9]
print(l)
list1=l[0:10:2] # kind of copy
# list1=[0, 2, 4, 6, 8]
print(list1)

# convert string to list
s='rajeev shivansh'
s=s.split()
print(s) # ['rajeev', 'shivansh']

# Accessing list element
l=[10, 20, 30, 'Veer', True, 30.7, 20+50j]
print(l[0])  # 10
print(l[3])  # Veer
print(l[-1]) # last item - (20+50j)
print(l[-2]) # 30.7

# Slicing in list
# by default step value is always 1 , start value-0, end- end of list
l2=[10, 20, 'preet', 20, 70.5, True, 30+70j]
print(l2[::]) # op-[10, 20, 'preet', 20, 70.5, True, (30+70j)]
print(l2[3::3]) # op- [20, (30+70j)]
print(l2[1:9:3]) # op- [20, 70.5]
print(l2[-1:-4:-2]) # op- [(30+70j), 70.5]
print(l2[-2::]) # [True, (30+70j)]

# Nested list -list inside list
lst2=[20, 30, 50, [77, 20, 60.8, ['free', True, 80,[10]]]]
# Accessing item from nested list
# indexing starts from 0
# again for sublist - indexing starts from 0
# first traverse in outer list to that index then again idexing starts from 0
print(len(lst2)) # It will give the number item present in list
# sublist will treat as 1 item for outer list
# here 0 index-20, 1 index-20, 2 index-50, 3 index-[77, 20, 60.8,['free'. True, 80, [10]]]
# if u want to fetch list data first traverse till that index
print(lst2[3]) # op-[77, 20, 60.8,['free'. True, 80, [10]]] Now traverse in this list
# again indexing starts from 0 index-77, 1st index-20, 2nd index- 60.8, 3rd index-['free', True, 80,[10]] 
print(lst2[3][3]) # op- ['free', True, 80, [10]] Now traverse in this list
# indexing - 0 index- 'free', 1 index- True, 2 index- 80, 3 index-[10] # this also sublist which has only one value 0 index-10
print(lst2[3][3][2]) # op- 80
print(lst2[3][3][3][0]) # 10

# Accessing list item of nested list
# No. of sub lists = no. of loops & loop-1 = if else condition
for item in lst2:
    if type(item) == list:  # Check if the item is a list
        for sub_item in item:
            if type(sub_item) == list:  # Check if sub_item is a list
                for sub_sub_item in sub_item:
                    if type(sub_sub_item) == list:  # Check if sub_sub_item is a list
                        for sub_sub_sub_item in sub_sub_item:
                            print(sub_sub_sub_item, end=" ")
                    else:
                        print(sub_sub_item, end=" ")
            else:
                print(sub_item, end=" ")
    else:
        print(item, end= " ")


lst=[10, 20, 30, 40, 'True', 'pet', True]
print(lst)
lst[0]=10
lst[6:]='sliced' # it will seperate all letters
print(lst)
lst[6:]= 'sliced data'
print(lst)
print(lst[-1])

# Addind data to list - append, extend
# append can add only one element at the end of list
l=[10, 20, 80, 90, 80, 90]
l.append(8) 
print(l)
l.append([20, 30]) # u can pass multiple data as list but it will store at the end as list
# l.append(20, 30, 40) # u will get error bcoz it accepts 1 argument

# extend can add one list at the end of list
list1=[30, 70]
l.extend(list1)
print(l)
l.extend([40, 80, 90])
print(l)

# insert(position, value)
list1.insert(1, "hamper")
print(list1)
print(list1.index("hamper")) # give the index position of value # return the first occurence of value


# Removing data from list - remove(value), pop()
l=[60, 90, 80, 70.6, 'yet']
l.pop() # Remove last item from list
print(l)
# l.pop(index) # Remove item from specied position
l.pop(2)

# remove(value) # we are passing one value if that value is not presnt will give you error else it will remove that value
# l.remove(9) # error if value not present
print(l)
l.remove(60) # value is present in list, it will remove that element
# if duplicate value is present it will remove the first occurence of value
print(l)
l.clear() # op- []  It removes elements from the list
l2=[9, 8, 7, 65, 98, 10]
del l2[3:] # delete all elements from index 3
print(l2)

# Functions of list-

lst_fun=[10, 20, 30, 80, 30, 50]
# count(value) - Returns the count of occurrences of x.
print(lst_fun.count(30)) 

# Sorting and Reversing
lst_fun.sort() # Sort element of list-Ascending to Descending
print(lst_fun)
lst_fun.reverse() # Descending to Ascending
print(lst_fun)
lst_fun.sort(reverse=True)
print(lst_fun)

# Copying list
lst=[10, 20, 30, 80]
lst2=lst.copy() # Returns a shallow copy of the list.
print(lst2)

# len(lst)	Returns the length (number of elements).	len(lst)
# max(lst)	Returns the maximum element.	max(lst)
# min(lst)	Returns the minimum element.	min(lst)
# sum(lst)	Returns the sum of all elements.	sum(lst)

# Operations on list-

# Concatenation/ Merging - Adding one list to another list like append function
lst1=[10, 20, 30, 40]
lst2=[10]
lst3=lst1+lst2
print(lst3)

# Muliplication / Replicating
lst3=lst1*3
print(lst3)

# Memebership Operator
print(20 in lst) # return boolean value - True or False
print(lst1 is lst2) # comparing memory location

# zip function - both list should contain same elements - Pair up tupe
lst1=[5, 12, 15, 7]
lst2=[14,5,7,90]
print(list(zip(lst1,lst2)))
print(tuple(zip(lst1, lst2))) 

lst3=[]

for i,j in zip(lst1,lst2):
    lst3.append(i+j)

print(lst3)

lst1=['A', 'app', '', 'da', 'kee', 't', 'doc', 'a']
lst2=['n', 'le', 'a', 'y', 'ps', 'he', 'tor', 'way']
lst3=[]
for i, j in zip(lst1, lst2):
    lst3.append(i+j)

# any and all function
lst=[10, 20, 30, -40, -50]
# using function
print(all([i>0 for i in lst]))
print(any([i>0 for i in lst]))
def any(lst):
    for i in lst:
        if i > 0:
            return True
    return False

def all(lst):
    for i in lst:
        if i<0:
            return False

    return True
print(any([-10, -20, -30, -40, -40]))
print(all([10, 20, 30, 40, -50]))

marks=[45, 75, 30, 80, 90]
print(all([x>35 for x in marks ]))
print(any([x>35 for x in marks ]))

# List Comprehension

# [expression for item in iterable if condition]
# expression: The operation to perform on each item.
# item: Variable representing each element in the iterable.
# iterable: The data structure being iterated over.
# condition (optional): A filter to include only certain items.

lst4=[x for x in range(1, 10)]
print(lst4)
print([x*x for x in range(1, 11)])
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # Op: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
numbers = [x if x % 2 == 0 else "Odd" for x in range(5)]
print(numbers)




# # # Program to print 
# # print("user")
# # user=int(input("Enter the number:"))
# # lst=[]# empty list
# # for i in range(user):
# #     lst.append(i**2)
# # print(lst)
# # lst=[20, 30, 40, 70, 70, 90, 10]
# # lst1=[]
# # lst1=[20, 30, 40, 70, 90, 10]

# # for i in lst:
# #     if i not in lst1: #50 not in lst1
# #         lst1.append(i)

# lst=[10, 20, 30, 50, 50, 70, 90, 50, 70, 90]
# lst1=[] #
# for i in lst:
#     if i not in lst1: # if i is not present in lst1 then only append data means i to lst1
#         lst1.append(i)
# # step i value is 10
# # now checking in our newlist if value is already present in new list
# lst1=[] # initially it is empty
# #if 10 is not present in lst1:
#     #then add that data into lst1
# # then will move to 20 , 30, 50
# lst1=[10, 20, 30, 50, 70, 90]
# # now 50 not in lst1 -> 
# # now i- value =50 if 50 not in lst1:

# # sum all the data of the list and 
# # "The sum of all the list data is sum_value"
# sum=0# initally value of sum is 0
# for i in lst1:
#     sum=sum+i









   





