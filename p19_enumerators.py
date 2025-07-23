'''
An enumerator is an object that adds a counter to an iterable.
It returns tuples containing the index and the corresponding element.
It's a convenient way to keep track of the index while iterating.
'''

# Create an enumerator using the enumerate() function.
# enumerate() takes an iterable as input and returns an enumerator object.'


my_list = ['apple', 'banana', 'cherry']

for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")

# Starting Index:-
# specify the starting index for the counter using the start parameter:

my_list = ['apple', 'banana', 'cherry']

for index, item in enumerate(my_list, start=1):
    print(f"Index: {index}, Item: {item}")