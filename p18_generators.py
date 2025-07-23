'''
A generator is a special type of iterator that uses a function with the yield keyword to produce a sequence of values.
Generators are memory-efficient because they generate values on demand, rather than storing the entire sequence in memory.
Generators are much easier to create than custom iterator classes.'
'''

def square(n):
    for i in range(n):
        yield i**2 #  [0  1 4 9 16]

for i in square(5): # for i in [0 1 2 4 9] 
    print(i)

print(square(5))


def square(n):
    for i in range(n):
        return i**2 #  [0  1 4 9 16]

print(square(5)) # for i in 0 
 

# generator

# def my_generator(data):
#     for item in data:
#         yield item * 2

# my_list = [1, 2, 3]
# my_gen = my_generator(my_list)

# for item in my_gen:
#     print(item)  # Output: 2 4 6


# my_list = [1, 2, 3]
# my_gen = (item * 2 for item in my_list)  # Generator expression

# for item in my_gen:
#     print(item)


'''---------------------------------------------------------------------------------------------------------------------------------------'''

# P1 Create customRange class with behaviour of range function

# class customRange:

#     def __init__(self, start, stop=None, step=1):
#         if stop is None:
#             self.start=0
#             self.stop=start
#         else:
#             self.start=start
#             self.stop=stop
#         self.step=step
#         self.current=self.start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if (self.current > self.stop and self.current >=self.step) or (self.current<self.stop and self.current<=self.step):
#             raise StopIteration
#         value=self.current
#         self.current+=1
#         return value
    
# cR=customRange(5, 10, 2)

'''---------------------------------------------------------------------------------------------------------------------------------------'''
