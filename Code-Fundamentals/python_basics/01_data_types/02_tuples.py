# Tuples - ordered, immutable, allows duplicates, allows mixed types

a = (1, 2, 3)
b = tuple()
c = tuple(range(5))          # (0, 1, 2, 3, 4)

# The classic trap — a single-element tuple needs a trailing comma
not_a_tuple = (5)            # int, 5          <- parentheses alone do NOT make a tuple!
real_tuple  = (5,)           # tuple, (5,)     <- the comma is what makes it a tuple

# Python doesn't look at the parentheses to decide "is this a tuple" — it looks at the comma. (5) is just the number 5 wrapped in math-style parens. You need (5,)

# Access (identical to list — read-only, never mutates)

# t = (10, 20, 30, 40, 50)
t[0]        # 10
t[-1]       # 50
t[1:3]      # (20, 30)
t[::2]      # (10, 30, 50)
t[::-1]     # (50, 40, 30, 20, 10)

# Update — not possible

t[0] = 999
# TypeError: 'tuple' object does not support item assignment

# Add — no .append/.insert/.extend, but + still works

t.append(60)

# AttributeError: 'tuple' object has no attribute 'append'

new_t = t + (60, 70)
print(new_t)   # (10, 20, 30, 40, 50, 60, 70)   <- a brand new tuple
print(t)        # (10, 20, 30, 40, 50)            <- t itself is untouched

# Remove — not possible

# The only two methods a tuple has

t2 = (10, 20, 10, 30)
t2.count(10)    # 2   — how many times 10 appears
t2.index(20)    # 1   — first position of 20

t3 = (1, [2, 3])

t3[1] = [99]
# TypeError: 'tuple' object does not support item assignment   <- as expected

t3[1].append(4)     # ...but this WORKS
print(t3)             # (1, [2, 3, 4])

t = (30, 10, 20)

sorted(t)              # [10, 20, 30]
print(type(sorted(t)))  # <class 'list'>   <- NOT a tuple!
print(t)                 # (30, 10, 20)     <- t itself unchanged

reversed(t)              # <reversed object at 0x...>   — an iterator, same as with list
list(reversed(t))         # [20, 10, 30]
tuple(reversed(t))         # (20, 10, 30)
print(t)                    # (30, 10, 20)   <- unchanged

t = (1, 2, 3, 4, 5)

sliced = t[::-1]
print(type(sliced), sliced)
# <class 'tuple'> (5, 4, 3, 2, 1)     <- a real, complete tuple, built right now

rev = reversed(t)
print(type(rev), rev)
# <class 'reversed'> <reversed object at 0x...>   <- NOT the values yet, just a "promise" to walk backward

print(list(rev))
# [5, 4, 3, 2, 1]     <- first time you ask, it gives you the values

print(list(rev))
# []                   <- second time, EMPTY!

print(sliced)
# (5, 4, 3, 2, 1)      <- still fine
print(sliced)
# (5, 4, 3, 2, 1)      <- still fine, as many times as you want

# sorted() gives you back a real, ordinary list — the same kind of object as [1, 2, 3]. There's nothing lazy or one-time about it. You can print it, loop over it, index into it, reuse it forever.
# reversed() is the odd one out — it gives you an iterator, a different kind of object that gets drained once and then is empty.