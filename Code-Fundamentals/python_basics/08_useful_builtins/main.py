"""
Useful Built-ins — Study Reference
Block 1, Topic 8: enumerate, zip, map, filter, any, all

Run this file top to bottom (python builtins_reference.py) — every
example prints its own output so you can see exactly what each one does.
"""

print("=" * 60)
print("1. enumerate() — get index + value together in a loop")
print("=" * 60)

fruits = ['apple', 'banana', 'cherry']

# manual way (before enumerate)
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1

print()

# enumerate way — no manual counter needed
for i, fruit in enumerate(fruits):
    print(i, fruit)

print()
print(list(enumerate(fruits)))   # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

print()
# enumerate with a custom start
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)


print()
print("=" * 60)
print("2. zip() — pair up multiple iterables at once")
print("=" * 60)

names = ['Alice', 'Bob', 'Carol']
ages = [30, 25, 35]
cities = ['NYC', 'LA', 'Chicago']

for name, age in zip(names, ages):
    print(name, age)

print()
print(list(zip(names, ages)))   # [('Alice', 30), ('Bob', 25), ('Carol', 35)]

print()
# zip with three iterables at once
for name, age, city in zip(names, ages, cities):
    print(name, age, city)

print()
# GOTCHA: zip stops at the SHORTEST iterable, silently, no error
short_names = ['Alice', 'Bob', 'Carol', 'Dave']
short_ages = [30, 25, 35]
print(list(zip(short_names, short_ages)))   # 'Dave' silently dropped


print()
print("=" * 60)
print("3. map() — apply a function to every item")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


result = map(square, numbers)
print(result)              # <map object at ...> -- lazy, not a list
print(list(result))        # [1, 4, 9, 16, 25]

print()
# with a lambda (most common form you'll actually see)
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

print()
# map with two lists at once — feeds one item from each into the function
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))   # [11, 22, 33]


print()
print("=" * 60)
print("4. filter() — keep only items that pass a test")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(x):
    return x % 2 == 0


result = filter(is_even, numbers)
print(result)              # <filter object at ...> -- lazy too
print(list(result))        # [2, 4, 6, 8]

print()
# with a lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

print()
# filter(None, ...) idiom — drops every falsy value in one line
mixed = [0, 1, '', 'hello', None, [], [1, 2], False, True]
print(list(filter(None, mixed)))   # [1, 'hello', [1, 2], True]


print()
print("=" * 60)
print("MAP vs FILTER — the core difference, side by side")
print("=" * 60)

nums = [1, 2, 3, 4, 5, 6]
mapped = list(map(lambda x: x * 10, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))

print('input:        ', nums)
print('map result:   ', mapped, '  <- SAME length as input, values CHANGED')
print('filter result:', filtered, '        <- FEWER items, values UNCHANGED')


print()
print("=" * 60)
print("5. any() / all() — check a condition across a collection")
print("=" * 60)

nums = [2, 4, 5, 8]
print('any even:', any(x % 2 == 0 for x in nums))   # True  - at least one is even
print('all even:', all(x % 2 == 0 for x in nums))   # False - not every one is even

print()
# any()/all() short-circuit: they stop the instant they know the answer
def check(x):
    print(f'  checking {x}')
    return x % 2 == 0


nums2 = [1, 3, 4, 5, 7]
result = any(check(x) for x in nums2)
print('result:', result)   # stops right after checking 4 -> never checks 5 or 7


print()
print("=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
enumerate(x)          -> (index, value) pairs
zip(x, y, ...)        -> pairs items from multiple iterables together (stops at shortest!)
map(func, x)          -> applies func to every item      -> SAME length as input
filter(func, x)       -> keeps only items where func(item) is True -> length <= input
any(bool_iterable)    -> True if AT LEAST ONE item is truthy (short-circuits)
all(bool_iterable)    -> True only if EVERY item is truthy (short-circuits)
""")