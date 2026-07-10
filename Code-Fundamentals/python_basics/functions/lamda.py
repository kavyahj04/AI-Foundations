lambda x : x ** 2

# def square(x): → lambda x: — instead of the word def and a function name, you just write the word lambda, and the parameter x goes right after it.
 
square = lambda x: x**2

# Edge case 1: a lambda can only ever be a single expression — no statements allowed inside it at all.

# lambda x: x = 5
# SyntaxError: cannot assign to lambda

# Edge case 2: the real reason lambda exists — passed directly as an argument, without ever being assigned a name.

words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=lambda w: len(w)))
# ['fig', 'kiwi', 'apple', 'banana']

# roughly what sorted does internally
keys = []
for item in words:          # this loop is inside sorted's C implementation
    keys.append(lambda_fn(item))   # calls your lambda, item becomes w
# then sorts `words` using those computed keys

# Compare to what you'd have to do without lambda:

def get_length(w):
    return len(w)

sorted(words, key=get_length)

# Edge case 3 — a lambda can take zero arguments:

say_hi = lambda: "Hi there!"
say_hi()
# 'Hi there!'

# Edge case 4 — a lambda can reach outside its own parameters and use a variable from the surrounding code, exactly like a normal function can:

tax_rate = 0.08
add_tax = lambda price: price + (price * tax_rate)
add_tax(100)   # 108.0

tax_rate = 0.15   # changed AFTER the lambda was created
add_tax(100)        # 115.0  <- uses the NEW tax_rate, not the one from when it was defined!

# Edge case 5 — you can assign a lambda to a name, but it's considered bad style once you do:

#  if it's important enough to have its own name, just write it as a real def, which also gives you a proper name in tracebacks if something goes wrong. Lambda earns its keep specifically when it's anonymous and inline — like the sorted(key=lambda...) case — not when it's sitting in a variable pretending to be a regular function.


# Lambda Gotcha 

funcs = [lambda: i for i in range(3)]

funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])

funcs = []
for i in range(3):
    funcs.append(lambda: i)   # each lambda just remembers "look up i later"
# after the loop, i == 2
print([f() for f in funcs])   # [2, 2, 2]

# ex - 1
funcs = [lambda x: x * 2 for i in range(3)]
print([f(10) for f in funcs])   # [20, 20, 20] -- correct, expected, no surprise

# Here x is the lambda's own parameter, supplied fresh at call time (f(10)). Each call gets its own x, so there's nothing shared to go stale. This isn't the gotcha — it's just normal function behavior.

message = "hello"
funcs = [lambda: message for i in range(3)]
print([f() for f in funcs])   # ['hello', 'hello', 'hello'] -- correct too!
