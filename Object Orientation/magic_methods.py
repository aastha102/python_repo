# Magic methods (also known as dunder methods — "double underscore") are special methods with __double_underscores__ on both sides.
# That let you customize the behavior of your own classes in Python.
'''
They power features like:
Operator overloading
Object creation
String representation
Iteration
Context management (like with)
Comparisons, etc.

Why Magic Methods Are Useful?

Enhance readability and make custom classes feel like built-in types.
Enable operator overloading, iteration, item access, etc.
Let you hook into Python’s built-in operations.
Essential for writing clean, idiomatic, and powerful Python code.

1. Object Creation & Destruction
__new__(cls[, ...])     # Called to create a new instance
__init__(self[, ...])   # Initializes instance (constructor)
__del__(self)           # Destructor; called when object is garbage collected

2. Operator Overloading
__add__(self, other)           # +
__sub__(self, other)           # -
__mul__(self, other)           # *
__matmul__(self, other)        # @
__truediv__(self, other)       # /
__floordiv__(self, other)      # //
__mod__(self, other)           # %
__divmod__(self, other)        # divmod()
__pow__(self, other[, modulo]) # **
__lshift__(self, other)        # <<
__rshift__(self, other)        # >>
__and__(self, other)           # &
__xor__(self, other)           # ^
__or__(self, other)            # |

Comparison Operators
__eq__(self, other)    # ==
__ne__(self, other)    # !=
__lt__(self, other)    # <
__le__(self, other)    # <=
__gt__(self, other)    # >
__ge__(self, other)    # >=

__str__(self)       # str(obj)
__repr__(self)      # repr(obj)
__bytes__(self)     # bytes(obj)
__format__(self, format_spec)
__hash__(self)      # hash(obj)
__bool__(self)      # bool(obj)
__int__(self)       # int(obj)
__float__(self)     # float(obj)
__complex__(self)   # complex(obj)
__index__(self)     # For slicing/indexing
__round__(self, n)  # round(obj, n)
__trunc__(self)
__floor__(self)
__ceil__(self)



'''
