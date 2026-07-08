# A list comprehension is a compact way to write the extremely common pattern "build a new list by transforming every item in an existing one." 
# 
# Instead of:
nums = [1, 2, 3]
squares_loop = []
for n in nums:
    squares_loop.append(n**2)
print(squares_loop)


squares_comp = [n**2 for n in nums]
print(squares_comp)

## syntax: [expression for item in iterable] — 
# read it left to right as "[give me expression, for each item in iterable]". 
# The expression is whatever you want to happen to each item before it lands in the new list.

# Adding a filter — if at the END, no else

nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in nums if n % 2 == 0]
# [2, 4, 6, 8]

# The if/else form — a different construct, easy to confuse with the filter

labels = ["even" if n % 2 == 0 else "odd" for n in nums]
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# This one sits at the start, before the for, and it transforms every item — nothing gets dropped, the output is always the same length as the input.

# The rule for telling them apart: 
# if after the for = filter (may shrink the list). 
# if/else before the for = transform (same length, always).

# Nested loops — and the classic use, flattening

pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict comprehension 

words = ["cat", "elephant", "dog", "hippopotamus"]
word_lengths = {w: len(w) for w in words}
# {'cat': 3, 'elephant': 8, 'dog': 3, 'hippopotamus': 12}

# Set comprehension — {expression for ...}, no colon

unique_lengths = {len(w) for w in words}
# {8, 3, 12}

## comprehensions don't leak their loop variable

x = 100
squares = [x**2 for x in range(5)]
print(x)   # 100  <- UNCHANGED!

y = 100
for y in range(5):
    pass
print(y)    # 4   <- a regular for loop DOES overwrite y

## A list comprehension runs in its own private scope — its loop variable never touches anything with the same name outside it. A regular for loop has no such protection; it happily overwrites an existing variable with the same name. This is a real, well-known Python 2→3 change and a fair interview question.

## Performance — comprehensions are a bit faster, and here's why

##  Python's for, if, while, and try blocks create no scope whatsoever.
#  The only things in Python that create a real, separate scope are: 
# functions (def), classes, and — as you just learned — comprehensions. 
# Proved it two ways:

if True:
    z = 50
print(z)   # 50   <- an if-block leaks too, not just for-loops!

def make_var():
    w = 999
make_var()
print(w)
# NameError: name 'w' is not defined   <- a FUNCTION actually does create scope

arr = ['a', 'b', 'c', 'd', 'e']    # len(arr) == 5
for i in range(len(arr)):
    pass
print(i)   # 4 -- last valid INDEX of a 5-element list, not 5