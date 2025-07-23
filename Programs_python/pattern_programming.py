# # Left aligned triangle
for i in range(5): # 0 1 2 3 4  # outer loop
    # 0 to 1 ->*
    for j in range(i+1):   # inner loop
        print("*", end=" ")
    print("")

# i=0 it goes into the inside the outer loop executing 4 to 6
# i 0 j = 0 to 1 , j=0 print("*" ) * print("") means go to next line
# 2nd iteration i= 1 , j=o to 2, 1st iteration of inner loop j=0 * j=1 * go to next line
# 3rd iteration i=2 , j=0 to 3 , j=0, 1, 2 * * * then will go to next line


# 1st iteration i=0 then will go for inner loop it executes complete inner loop then procced the next value of i
# i=0 , j=0to i+1= 0 to 1, j=0
# i=1, j=0 to i+1=0 to 2, j=0, 1
# i=2 , j=0to i+1= 0 to 3, j=0, 1, 2
# i=3, j=0 to i+1=0 to 4, j=0, 12, 3
# i=4, j=0 to i+1=0 to 5, j=0, 1, 2, 3, 4
    # 1st iteration we are strting from outer loop
    # 1st iteration  i value 0 will go to inner loop j->0 to 1=1-0j= 0-> *
    # 2nd iteration i value 1 will go to inner loop j->0 + i=1+1-> j=0,1-> **
    # 3rd iteration i value 2 will go to inner loop j-> 0 to i-1=2+1=3, j=0,1,2 ->* * *
    # 4th iteration i value 3 will go to inner loop j-> 0 to i+1=4-> j=0, 1, 2, 3->* * * *
    # 5th iteration i value 4 will go to inner loop j-> 0 to i+1= 5-> j=0, 1, 2, 3, 4-> * * * * *

# Right aligned triangle
for i in range(5): # outer loop
    for k in range(4,i,-1): # 1st inner loop
        print(" ", end=" ")
    for j in range(i+1): #  2nd inner loop
        print("*", end=" ")
    print("") # part of outer loop

    # execution begins from outer loop then go for inner loop and complete the loop and statement/ part of outer loop then go for next iteration of outer loop

# 1st iteration i=0 we want 4 space 5 to i= 5 to 0, k=,4 to 0-> k=4 , 3, 2, 1 j=0to1->j=0
# 2nd iteration i=1 then wit will go on inner loop k =4 to 1, k->4, 3, 2 j= o to 2->j=0, 1
# 3rd iteration i=2 then will go on inner loop k=4 to 2, k->4, 3, j=0, 1, 2
# 4th iteration i=3 then will go on inner loop k= 4 to 3 k->4 j=0, 1, 2, 3
# for i in range(5):
#     print("*" * i)


# for i in range(5):
#     print(" " * (5 - i) + "*" * i)


# for i in range(5):
#     print(" " * (5 - i) + "*" * ((2 * i) - 1))

[print(" " * (5 - i) + "*" * ((2 * i) - 1)) for i in range(5)]

num=1
for i in range(5): # 0 1 2 3 4 
    # 0 to 1 ->*
    for j in range(1,i+2): 
        print(num, end=" ")
        num=num+1
    print("")



# 1st iteration when i =0, j=0 to 1 , j=0 1 num=num+1= 1+1=2 
# 2nd iteration when i=1, j= 0 to 2, j= 0 num=2 , num=2+1=3 j=1 num=3 , num=4
# 3rd iteration when i=2 , j=0 to 3, j=0 num=4, num=4+1=5 j=1 5 num=5+1=6  print 6 then increment num=7
# 4th iteration when i=3 , j= 0 to 4, j=0  num=7 num=7+1=8 j=1 8 num=9 j=2 9 num=10 j=2 10 then increment num=num+1 =10+1=11
# 5 th iteration when i=4, j=0 to 5, j=0 11 num=12, j=1 12 num=13, j=2 13 num=14, j=3 14 num=15, j=4 15 num=16 

