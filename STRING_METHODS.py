s = "hello world"

# 1. Case Handling Methods

print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.capitalize())  # Hello world
print(s.title())       # Hello World
print(s.swapcase())    # HELLO WORLD → hello world
print("HELLO".islower())  # False
print("Hello".istitle())  # True

#  2. Searching & Checking

print(s.startswith("hello"))  # True
print(s.endswith("world"))    # True
print(s.find("o"))            # 4 (index of first 'o')
print(s.rfind("o"))           # 7 (last 'o')
print("123abc".isalnum())     # True
print("abc".isalpha())        # True
print("123".isdigit())        # True
print(" ".isspace())          # True

#  3. Trimming & Stripping
s = "   hello world   "

print(s.strip())       # "hello world"
print(s.lstrip())      # "hello world   "
print(s.rstrip())      # "   hello world"
print("hello!!!".rstrip("!"))  # "hello"

# 4. Replacing & Modifying
s = "banana"

print(s.replace("a", "A"))          # bAnAnA
print(s.replace("a", "A", 2))       # bAnAnA (only first 2)
print("hello".zfill(10))            # "00000hello"

#  5. Joining & Splitting
words = ["Python", "is", "awesome"]
print(" ".join(words))             # "Python is awesome"

s = "Python,is,awesome"
print(s.split(","))                # ['Python', 'is', 'awesome']

print("line1\nline2".splitlines()) # ['line1', 'line2']

# 6. Alignment and Padding
s = "hi"

print(s.center(10, "*"))  # ****hi****
print(s.ljust(10, "-"))   # hi--------
print(s.rjust(10, "."))   # ........hi

# 7. Encoding and Translating
s = "hello"
print(s.encode())  # b'hello'

# Translation example
trans = str.maketrans("aeiou", "12345")
print("hello".translate(trans))  # h2ll4

'''   Explaination
trans = str.maketrans("aeiou", "12345")
This creates a translation table that maps:

'a' → '1'
'e' → '2'
'i' → '3'
'o' → '4'
'u' → '5'
It returns a dictionary-like table used by .translate()

text = "hello"
trans = str.maketrans("aeiou", "12345")
print(text.translate(trans))  # Output: h2ll4
1. Characters in "hello":
'h' → not in table → remains 'h'
'e' → mapped to '2'
'l' → not in table → remains 'l'
'l' → same
'o' → mapped to '4'

'''

# removeprefix() and removesuffix()
s = "unwanted_text"

print(s.removeprefix("un"))   # wanted_text
print(s.removesuffix("_text"))  # unwanted