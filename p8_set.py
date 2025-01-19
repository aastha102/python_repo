# Set
#A set is an unordered, mutable, and unindexed collection of unique elements.
# Unordered – No guarantee of element order.
# Unique Elements – Duplicate values are automatically removed.
# Mutable – You can add or remove elements.
# Unindexed – Cannot access elements using an index.

# empty set decalartion
s=set()
print(s)
s={} # we can not declare empty set
# it stores only unique elements 
# set does not supports indexing, slicing, fetching
print('r' *10)
s={10, 20, 30, 40}
print(s)
s1={10, 20, 30, 40, 10} # if we pass any duplicate it will not consider that value
print(s1)

# converting into set
s1=set(s)
print(s1)

# functions of set
print('$' *9)
s1.add(35) # it takes only single value
print(s1)
s1.update({10, 20, 30})
print(s1)
print('@' *20)
s={10, 20, 30, 40}
# Removing of data from the set
s.remove(20) #error if not present
print(s)
s.discard(20) # won't throw error at any condition
print(s)
s.clear() # Remove all elements from the set
print(s)

# Set operations

s1={10, 20, 30, 40, 50}
s2={50, 55, 60 , 65}
s=s2.union(s1) # combine all element s | s1
print(s)

print('^' * 10) 
s=s2.intersection(s1) # symbol:&
print(s)
s=s2 & s1
print(s) # common elements

s2=s2.difference(s1) # - It will include s2 elements which is not present in s1
print(s2)
s2=s2-s1 # we are removing that element from s2 which is present in s1
print(s2) 

s1={10, 20, 30, 40, 50}
s2={50, 55, 60 , 65}
s2=s2^s1
print(s2)
s2=s2.symmetric_difference(s1)
print(s2) # Either x or y but not in both , It will include not common elements

s1={10, 20, 30, 40, 50, 80, 70}
s2={50, 55, 60 , 65, 77, 90}
# symmetric_difference_update() does not return a value; it updates the set s2 in place and returns None.
s5=s2.symmetric_difference_update(s1)
print(s5) # op-None
s2.symmetric_difference_update(s1)
print(s2)

s1 = {10, 20}
s2 = {10, 20, 30, 40}

print(s1.issubset(s2))  # True (s1 is a subset of s2)
print(s2.issuperset(s1))  # True (s2 is a superset of s1)
print(s1.isdisjoint({50, 60}))  # True (no common elements)

# Frozen Set
# It is an immutable version of a set.
# frozenset cannot be modified after creation.

# Empty frozenset
empty_fs = frozenset()

fs = frozenset([10, 20, 30])
print(fs)  # Output: frozenset({10, 20, 30})

# fs.add(40)  # error - 'frozenset' object has no attribute 'add'
# It supports all the set operations- union, intersection etc.


