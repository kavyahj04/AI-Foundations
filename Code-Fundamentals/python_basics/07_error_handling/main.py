# print('before')
# result = 10 / 0
# print('after')
result = 0
print('before')
try:
    result = 10 / 0
except:
    print('something went wrong')
    print(result)
print('after')

data = {'apple': '1.50', 'banana': '0.75'}

def get_price(data, key):
    try:
        value = data[kye]   # typo: 'kye' instead of 'key' — a real bug in the code
        return float(value)
    except (KeyError, ValueError):
        print('Price not found or invalid')
        return 0.0

# print(get_price(data, 'apple'))

try:
    print(1/0)
except ZeroDivisionError:
    print('caught it!')
print("This works")

# try:
#     print(1/0)
# except ValueError:
#     print('caught it!')

# my_list[10] raises IndexError, but except KeyError]

my_list = [1, 2, 3]
try:
    print(my_list[10])
except IndexError:
    print('caught it!')

try:
    int('not a number')
except (ZeroDivisionError, ValueError):
    print('caught it!')

#3 — else. Runs only if try had zero errors:

try:
    print(10 / 2)
except ZeroDivisionError:
    print('error!')
else:
    print('no error happened')

try:
    print(10 / 0)
except ZeroDivisionError:
    print('error!')
# lse means "only if try was completely clean, no exception at all
else:
    print('no error happened')

# finally. Runs no matter what:

try:
    print(10 / 2)
except ZeroDivisionError:
    print('error!')
finally:
    print('this always runs')

try:
    print(10 / 0)
except ZeroDivisionError:
    print('error!')
finally:
    print('this always runs')


def test():
    try:
        return 1
    finally:
        print('finally still runs, even with a return above it')

print('function returned:', test())

#4 — raise. You create and throw an error on purpose, exactly like the built-in ones:


def set_age(age):
    if age < 0:
        raise ValueError('age cannot be negative')
    print('age set to', age)

# set_age(25)
# set_age(-5)

try:
    set_age(-5)
except ValueError as e:
    print('caught:', e)

def process():
    try:
        set_age(-5)
    except ValueError as e:
        print('logging the error:', e)
       # raise   # uncomment to see how it works # re-raise the SAME exception

process()


class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        # pass
        raise InsufficientBalanceError(f'Cannot withdraw {amount}, balance is {balance}')
    return balance - amount

# withdraw(100, 500)

try:
    withdraw(100, 500)
except InsufficientBalanceError as e:
    print('caught:', e)

print(issubclass(InsufficientBalanceError, Exception))

