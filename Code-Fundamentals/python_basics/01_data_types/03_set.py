# Create

a = {1, 2, 3}
b = set()
c = set([1, 2, 2, 3])     # from a list -- dupes vanish
print(c)                    # {1, 2, 3}

d = set("hello")            # from a string -- unique CHARACTERS, one per letter
print(d)                     # {'o', 'h', 'e', 'l'}   <- only 4, the two 'l's collapse into one

# Access — no indexing, no slicing

s = {10, 20, 30}
s[0]
# TypeError: 'set' object is not subscriptable

20 in s     # True
99 in s     # False

# Adding elements
s = {10, 20, 30}
s.add(40)
print(s)               # {40, 10, 20, 30}

s.update([50, 60])      # add MULTIPLE items from any iterable
print(s)                  # {40, 10, 50, 20, 60, 30}

s.update({70, 80})        # works with another set too
print(s)                    # {70, 40, 10, 80, 50, 20, 60, 30}

# Removing elements

s = {10, 20, 30}
s.remove(20)
print(s)                 # {10, 30}

s.remove(999)
# KeyError: 999           <- errors if the value isn't there

s.discard(999)             # same idea, but silent if missing
print(s)                     # {10, 30}   <- no error this time

popped = s.pop()
print(popped, s)              # 10  {30}   <- removes something arbitrary (no order, no control over which)

s.clear()
print(s)                        # set()

# .remove() vs .discard() is a real interview question: .remove() throws if the value is missing, .discard() doesn't. Use .discard() when "might already be gone" is a normal case, .remove() when its absence should be treated as a bug.

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

x | y     # {1, 2, 3, 4, 5, 6}   -- union: everything in either
x & y     # {3, 4}               -- intersection: only what's in both
x - y     # {1, 2}                -- difference: in x, NOT in y
y - x     # {5, 6}                 -- difference is NOT symmetric — order matters
x ^ y     # {1, 2, 5, 6}            -- symmetric difference: in exactly one, not both

{1, 2}.issubset(x)       # True
x.isdisjoint({100})       # True  -- no elements in common - isdisjoint() is really just asking "is the intersection empty?

a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

a.isdisjoint(b)   # True   -- zero overlap
a.isdisjoint(c)    # False  -- they share 3
a & c              # {3}     -- this is WHY it's False