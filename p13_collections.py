from collections import Counter, deque, namedtuple, defaultdict, UserList

import collections

# 1. Counter - A Counter is a dictionary subclass used for counting hashable objects. Counting occurrences of items in a iterators) like list or string.
lst=['a', 'a', 'b', 'c', 'd', 'd']
print(Counter(lst))

print(lst.count('a'))

d={} # empty dictionary
for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

# Merging the dictionary  
d1={'a':1, 'b':2}
d2={'c':3, 'd':4}
d3={'e':5, 'f':6}
d4={**d1, **d2, **d3}
print(d4)
d4['a']=20
print(d4)
print(d1)

# 2. ChainMap - A ChainMap groups multiple dictionaries into a single unit, allowing lookups across them. Combining multiple dictionaries while keeping them separate.
d4=collections.ChainMap(d1, d2, d3)
print(d4)
d4['a']=30
print(d4)
print(d1)

# 3. Deque - A deque (pronounced "deck") is a list-like data structure optimized for fast appends and pops from both ends.
dq=deque(['name', 'age', 'place'])
dq.append('read')
print(dq)
dq.appendleft('write')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)

# 4. namedtuple - A subclass of tuple from the collections module. Allows accessing elements by both index and attribute name.

# Defining a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating an instance
p1 = Person(name='Alice', age=25, city='New York')

# Accessing values using attribute names
print(p1.name)  # Output: Alice
print(p1.age)   # Output: 25
print(p1.city)  # Output: New York

# Accessing values using index (like a normal tuple)
print(p1[0])  # Output: Alice

# Tuples and namedtuples are immutable
# p1.age = 30  # TypeError: can't set attribute

# 5. defaultdict - A defaultdict automatically provides a default value when a key is missing.

# defaultdict with list as default factory
dd = defaultdict(list)

# Appending values without initializing key
dd['fruits'].append('apple')
dd['fruits'].append('banana')

print(dd)  
# Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

print(dd['vegetables'])  
# Output: [] (Instead of KeyError, it gives an empty list)


class MyUserList(UserList):
    def append(self, item):
        print(f"Adding {item} to list")
        super().append(item)

ul = MyUserList([1, 2, 3])
ul.append(4)

print(ul)
# Output:
# Adding 4 to list
# [1, 2, 3, 4]

ul.extend([5, 6])  
print(ul)  
# Output:
# Adding 5 to list
# Adding 6 to list