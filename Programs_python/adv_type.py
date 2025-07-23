from collections import Counter

# Remove all occurence of elements
lst=[1, 2, 3, 4, 2, 1, 0, 6, 9]
cnt=Counter(lst)
print(cnt)
'''
new_list=[]
for k, v in cnt.items():
    if v>1:
        new_list.append(k)
'''
new_l=[k for k, v in cnt.items() if v>1]
print(new_l)
lst=list(set(lst)-set(new_l))
print(lst)

# First repeating character in a string
str="abccdddde" 
# str1=str.split()
cntr=Counter(str) # Counter[{a:1, b:1, c:2, d:4, e:1}]
print(cntr.items())
for k, v in cntr.items():  #1st iteration k=a, v=1
    # if v>1:
    if v==1: 
        print(k, v)
        break 
print(cntr.items())

# Most repeating character
most_common = max(cntr.items(), key=lambda x: x[1])
print("Most repeating character:", most_common[0], "Count:", most_common[1])

# Most common characters
str_="aabbcccdddde"
cntr=Counter(str_)
print(cntr.most_common(1)) # 1st most common
print(cntr.most_common(2)) # 2nd most common

# Last non repeating character
for i in reversed(str):
    if cntr[i]==1:
        print(i, cntr[i])
        break

str="a2b3c4" # aabbbcccc

# alpha_l=[]
# digit_l=[]
# for i in str:
#     if i.isalpha():
#         alpha_l.append(i)
#     elif i.isdigit():
#         digit_l.append(i)
alpha_l=[i for i in str if i.isalpha()]
digit_l=[int(i) for i in str if i.isdigit()]
# print(alpha_l)
# print(digit_l)     
newlist=[ i*j for i,j in zip(alpha_l, digit_l)]   
# print(newlist)
# for i,j in zip(alpha_l, digit_l):
#     newlist.append(i*int(j))
# print(newlist)
print("".join(newlist))

# Move all zereos to the end
lst_all_zero=[1, 0, 2, 0, 7, 8, 0, 9] #[1,2,7,8,9,0,0,0] 
zereos=[x for x in lst_all_zero if x==0]
non_zeroes=[x for x in lst_all_zero if x!=0]
lst_all_zero=non_zeroes+zereos
print(lst_all_zero)

str="20"
a_in=20
del str # deleting from the memory
print(str(a_in))

