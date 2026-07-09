# STRING OPERATIONS 

# ordered, immutable (same rule as tuple), indexable, hashable (because it's immutable — same rule as before, showing up a fourth time now).

# Access 

s = "Hello World"
s[0]        # 'H'
s[-1]       # 'd'
s[0:5]      # 'Hello'
s[6:]       # 'World'
s[::-1]     # 'dlroW olleH'   -- same reverse trick as list/tuple

# s[0] = 'h'
# TypeError: 'str' object does not support item assignment

# Strings can never be edited in place — every "modification" (.upper(), .replace(), etc.) 
# hands you back a brand-new string, leaving the original untouched.\
# This is also why a string is hashable and safe to use as a dict key — same immutability → hashability rule you already know, now confirmed for a fourth data type.

name = "Kavya"
score = 95.5678

f"Hello {name}, your score is {score}"
# 'Hello Kavya, your score is 95.5678'

f"Rounded: {score:.2f}"
# 'Rounded: 95.57'          <- :.2f formats to 2 decimal places

f"Expression inside: {2 + 2}"
# 'Expression inside: 4'     <- anything inside {} is a real Python expression

f"Uppercase inline: {name.upper()}"
# 'Uppercase inline: KAVYA'   <- even method calls work inside {}

# Split
"the cat sat".split()          # ['the', 'cat', 'sat']    -- default: split on any whitespace
"a,b,,c".split(",")              # ['a', 'b', '', 'c']       -- keeps empty strings between separators
"a,b,c,d".split(",", 1)           # ['a', 'b,c,d']             -- maxsplit limits how many splits happen

# .join() — list to string, the inverse of split

",".join(["a","b","c"])    # 'a,b,c'
"".join(["a","b","c"])      # 'abc'
" ".join(["the","cat","sat"])  # 'the cat sat'

# strip() family — trimming from the ends only

"   hello   ".strip()      # 'hello'          -- removes whitespace from both ends
print("xxxyhelloxxzzzz".strip("xyz"))      # 'hello'           -- removes the given characters, not a substring match
"   hello   ".lstrip()        # 'hello   '         -- left only
"   hello   ".rstrip()         # '   hello'          -- right only

# Other everyday methods

s = "Hello World"
s.lower()               # 'hello world'
s.upper()                # 'HELLO WORLD'
s.replace("World","Python")  # 'Hello Python'   -- returns new string, doesn't mutate s
s.find("World")            # 6                    -- index of first match
s.find("xyz")                # -1                    -- NOT an error, just -1 if missing
s.startswith("Hello")          # True
s.endswith("World")              # True

result = ""
for p in parts:
    result += p
# 44.10 ms  for 20,000 pieces

result2 = "".join(parts)
# 0.37 ms   -- roughly 120x faster