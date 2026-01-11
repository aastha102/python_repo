from collections import Counter, deque, namedtuple, defaultdict, UserList, OrderedDict

import collections

# 1. Counter - A Counter is a dictionary subclass used for counting hashable objects.
# Counting occurrences of items in a iterators) like list or string.
lst=['a', 'a', 'b', 'c', 'd', 'd']
c="aaabbbaccbdddd"
print(Counter(lst)) 
dict=Counter(c)
print(type(dict))
print(dict.values())
print(dict.most_common(1)) # 1st most common character [('a', 4)], for 2nd most common (2)
print(dict.most_common(2)[0]) #('a', 4) coz it is present in 0th index of collection
print(dict.most_common(1)[0][0])  
print(list(dict.elements()))

# Without using counter
lst1=[]
d={} # empty dictionary
for i in lst: # ['a', 'a', 'b', 'c', 'd', 'd'] # checking a
    if i not in d:#lst1 
        d[i]=1 #d[a]=1 d[key]=value # 2nd iter a  d['a']=1  ->d={'a':2, 'b':1} d['a']=1+1=2
    else:
        d[i]+=1 #1+1
print(d)

# Merging the dictionary  
d1={'a':1, 'b':2}
d2={'c':3, 'd':4}
d3={'e':5, 'f':6}



d4={**d1, **d2, **d3} 
print(d4)
d4['a']=20 # doesn't reflect on original one
print(d4)
print(d1)

# 2. ChainMap - A ChainMap groups multiple dictionaries into a single unit, allowing lookups across them. 
# Combining multiple dictionaries while keeping them separate.
d4=collections.ChainMap(d1, d2, d3)
print(d4)
d4['a']=30 # reflect on original one
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
Person = namedtuple('Person', ['name', 'age', 'city']) # Class, attributes
# Creating an instance
p1 = Person(name='Alice', age=25, city='New York')
p2=Person("Govind", 30, 'Japan')

# Accessing values using attribute names
print(p1.name)  # Output: Alice
print(p1.age)   # Output: 25
print(p1.city)  # Output: New York
print(p2.name, p2.age, p2.city)
# Accessing values using index (like a normal tuple)
print(p1[0])  # Output: Alice

 # Tuples and namedtuples are immutable
# p1.age = 30  # TypeError: can't set attribute

# 5. OrderedDict is a class from the collections module in Python that remembers the order in which keys are inserted into a dictionary.

# Before Python 3.6, the built-in dict did not guarantee order of items. So, if you wanted a dictionary that maintains insertion order, you used OrderedDict.
# From Python 3.7 onwards, regular dict maintains insertion order by default, but OrderedDict is still useful when you need:
# Advanced operations like reordering items
# Comparing dictionaries based on order
# Using special methods not available in dict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#Useful Methods of OrderedDict:
#move_to_end()
od.move_to_end('a')  # Moves 'a' to the end
#popitem(last=True)
# Pops the last inserted item if last=True (default)
# Pops the first inserted item if last=False
od.popitem()        # Remove last item
od.popitem(False)   # Remove first item


# 6. defaultdict - A defaultdict automatically provides a default value when a key is missing.

# defaultdict with list as default factory
dd = defaultdict(list) # if key is not there it provides [] list for that key

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