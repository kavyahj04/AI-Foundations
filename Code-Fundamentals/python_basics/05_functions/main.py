# Default arguments

def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
    return f"{greeting}, {name}"

greet("Kavya")
greet("Mayur", "Hey There!!")
greet("Kavya", greeting="Good morning")

# Mutable Default Argument

##  a default value in a function signature is built once, when Python reads the 
# def line — not fresh on every call. 
# If that default is something mutable (list, dict, set) and the function changes it in place, 
# every call that skips that argument shares and permanently affects the same object.

def add_item(item, basket=[]):
    basket.append(item)
    print(basket)

# add_item("apple")    # ['apple']
# add_item("banana")     # ['apple', 'banana']   <- keeps growing across calls!

def add_item2(item, name="Hello"):
    name = item
    print(name)

add_item2("kavya")    
add_item2("mayur")     

def add_item_fix(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    print(basket)

# *args - when you don't know in advance how many positional values someone will pass in 
# *args scoops up any number of them into one tuple.

def total(*args):
    print(sum(args))


total(1, 2, 3)   # args = (1, 2, 3)  -> 6
total(7)           # args = (7,)        -> 7
total()             # args = ()          -> 0

# Edge case 1 — combining required params with *args

def describe(first, *rest):
    print('first:', first, '| rest:', rest)
    

describe('a', 'b', 'c', 'd')
# first: a | rest: ('b', 'c', 'd')

describe('a')
# first: a | rest: ()   <- only one value given, rest is just empty

def describe2(first, *rest):
    print('first:', first, '| rest:', rest)
    print([n * n for n in rest[0]]) 
    

describe2([1,2,3,4], [1,2])

# Edge case 2 — unpacking a list INTO a call using *

nums = [10, 20, 30]

def total(*args):
    return sum(args)

#total(*nums) scatters the list into 3 separate loose values (not yet a tuple, just 3 plain arguments)
total(*nums)
# 60

# Edge case 3 — the name args is just convention, not special:


# Edge case 4 — keyword arguments do NOT go into *args
def show(*args, name):
    print(args)
    print(name)

show(1, 2, name="Kavya")
# TypeError: show() got an unexpected keyword argument 'name'

# kwargs 

# just like *args catches extra positional values into a tuple, **kwargs catches extra keyword values into a dict — for when you don't know in advance which named arguments someone will pass.


def describe(**kwargs):
    print(kwargs)

describe(name="Kavya", role="engineer", level="senior")
# {'name': 'Kavya', 'role': 'engineer', 'level': 'senior'}

# Edge case 1: combining required param with kwarg

def describe(name, **details):
    print('name:', name, '| details:', details)

describe('Kavya', role='engineer', level='senior')
# name: Kavya | details: {'role': 'engineer', 'level': 'senior'}

# Edge case 2: unpacking a dict into a call
config = {'temperature': 0.7, 'max_tokens': 500}

def call_model(**kwargs):
    print(kwargs)

call_model(**config)
# {'temperature': 0.7, 'max_tokens': 500}

# instead of collecting keyword arguments into a dict, it spreads a dict out into separate keyword=value pairs at the call site. This is exactly the model.generate(**config) pattern from real AI code.

# Two ways to fill *args:

# Direct: total(10, 20, 30) — type loose values right in the call.
# Indirect: nums = [10, 20, 30] then total(*nums) — build a list first, unpack it in the call.
# Both end up identical inside the function: args = (10, 20, 30).

# Two ways to fill **kwargs:

# Direct: call_model(temperature=0.7, max_tokens=500) — type key=value right in the call.
# Indirect: config = {'temperature': 0.7, 'max_tokens': 500} then call_model(**config) — build a dict first, unpack it in the call.


# Edge case 4: positional arguments cannot be caught by kwargs

# *args = extra positional values → tuple. **kwargs = extra keyword values → dict. Same idea, different argument shape.

# Unpacking 

def total(a, b, c):
    return a + b + c

nums = [1, 2, 3]
total(*nums)       # 6   -- spreads the list into 3 separate positional args

info = {'a': 10, 'b': 20, 'c': 30}
total(**info)        # 60  -- spreads the dict into 3 separate keyword args

# Edge cases: mixing unpacking with explicit args, and combining list+dict unpacking

nums = [2, 3]
total(1, *nums)   # 6  -- 1 fills 'a' directly, *nums fills b and c

def full(a, b, c, d, e):
    return (a, b, c, d, e)
full(*[1, 2], **{'c':3, 'd':4, 'e':5})
# (1, 2, 3, 4, 5)

# Edge cases: unpacking with wrong count and mismatched dict keys
total(*[1, 2])            # TypeError: missing 1 required positional argument: 'c'
total(*[1, 2, 3, 4])         # TypeError: takes 3 positional arguments but 4 were given
total(**{'a':1,'b':2,'z':3})   # TypeError: unexpected keyword argument 'z'

def full_signature(a, b, *args, c=10, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

full_signature(1, 2, 3, 4, 5, c=99, extra="hello")
# a=1, b=2, args=(3, 4, 5), c=99, kwargs={'extra': 'hello'}

full_signature(1, 2)
# a=1, b=2, args=(), c=10, kwargs={}

full_signature(1, 2, 3, 4, 99)
# a=1, b=2, args=(3, 4, 99), c=10, kwargs={}   <- 99 got swallowed into args!

full_signature(1, 2, 3, 4, c=99)
# a=1, b=2, args=(3, 4), c=99, kwargs={}         <- this is the only way to actually set c

def f(a, b, c=9, *args):
    print(f"a={a}, b={b}, c={c}, args={args}")

f(1, 2, c=9)          # a=1, b=2, c=9, args=()      <- c set by keyword, fine
f(1, 2, 3)             # a=1, b=2, c=3, args=()      <- c set positionally!
f(1, 2, 3, 4, 5)       # a=1, b=2, c=3, args=(4, 5)  <- 3rd positional grabs c, rest overflow to args
# So the rule you derived — "once you're past *args, keyword is the only way in" — is specific to params declared after a bare *args (or *). Order matters like this:

# Positional params (a, b) — filled left to right by position or keyword.
# A param with a default before *args (like c=9 here) is still positional-or-keyword — a stray positional argument can still land in it, silently, which is arguably worse than being swallowed by *args.
# Once you write a bare *args (or a lone *), everything declared after it becomes keyword-only — no positional argument can ever reach it, so it either gets its default or must be passed by name.
# **kwargs mops up any keyword arguments that didn't match a named parameter.
# That's why your full_signature(a, b, *args, c=10, **kwargs) behaves the way it does: c comes after *args in the signature, so it's locked to keyword-only — positional overflow can never touch it, it always either gets its default or requires c=.

# If you moved c before *args instead (def f(a, b, c=10, *args, **kwargs)), you'd get the "silently grabbed positionally" behavior instead — usually the more surprising/bug-prone version, which is exactly why *args, c=10 (keyword-only) is the safer pattern when you want args to be pure catch-all and c to be explicit.

