# In Python, an iterator is an object that implements the iterator protocol, which consists of two methods:

# __iter__() – Returns the iterator object itself. It's called when you use iter() on an object.
# __next__() – Returns the next value from the sequence. When there are no more items, it raises a StopIteration exception.

lst=[10, 20, 30, 40, 50, 60]

# -> 10 20 30 40 50 60

# create iterator using iter keyword
iterable=iter(lst)
print(iterable, type(iter))

# getting the data of iterator-

# ways to fetch the data of iterator - for loop, __next__() or next keyword
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
# print(iterable.__next__())
# print(next(iterable))
# print(iterable.__next__())
# print(iterable.__next__()) # Raise an exception 

# while True:
#     print(iterable.__next__())

while True:
    try:
        item = next(iterable)  # Get the next item
        print(item)
    except StopIteration:
        break 

for i in iterable:
    print(i)

# [Note: Only { for loop } can eliminate the problem of raising StopIteration exeption]

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [1, 2, 3]
my_iterator = MyIterator(my_list)

for item in my_iterator:  # Behind the scenes, Python uses iter() and next()
    print(item)
    

'''------------------------------------------------------------------------------------------------------------------------------------'''

def iterator(lst):
    item=list(lst)
    for i in range(len(item)-1, -1, -1 ):
        yield item[i]
