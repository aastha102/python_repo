# # Print the items from the list which length user entered.
# lst=['water', 'cat', 'kent', 'red',]
# lst1=[]
# count=0
# print(lst)
# n=int(input("Enter the length"))
# for x in lst:
#     if len(x) is n:
#         count=count+1
#         lst1.append(x)
# print(count)
# print(lst1)

# Swapping of first and last element of list
lst=[10, 20, 30, 40, 50]
temp=lst[0]
lst[0]=lst[len(lst)-1]
lst[len(lst)-1]=temp
print(lst)

# Remove all occurence of value
lst_alpha=['Heer', 'Great', 'Great', 'Bet']
while lst_alpha.count('Great'):
    lst_alpha.remove('Great')
print(lst_alpha)

# Remove last occurence of value
lst_alpha=['Grip','Heer', 'Great', 'Great', 'Bottle', 'Great', 'Bet']
for i in range(len(lst_alpha)-1, -1, -1):
    print(lst_alpha[i])
    if lst_alpha[i] =='Grip':
        del lst_alpha[i]
        break
print(lst_alpha)

# Print data like- name-Riya age-20 date-20/2/2025
tup=(["name", "age", "date"], ["Riya", 20, "20/2/2025"])
print(len(tup[0]))
for fetch in range(len(tup[0])):
    print(tup[0][fetch] , "-" , tup[1][fetch])
# using zip()-> it go minimum length
for t0, t1 in zip(tup[0], tup[1]):
    print(t0, "-" , t1)
print(list(zip(tup[0],tup[1])))
o=list(zip(tup[0],tup[1]))
print(dict(o))

