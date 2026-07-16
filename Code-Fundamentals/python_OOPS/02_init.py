# __init__ isn't what builds the object — it only fills in data on an object that already exists

# Exactly right. __init__ doesn't create anything — the object already exists by the time __init__ runs. All it does is take that already-existing, still-empty object and fill in its starting values.

# How self gets bound under the hood

acc1 = Account("Kavya", 100)

print("acc1.deposit    ->", acc1.deposit)
print("Account.deposit ->", Account.deposit)

# Output:
# acc1.deposit    -> <bound method Account.deposit of <__main__.Account object at 0x7ff2a8bff530>>
# Account.deposit -> <function Account.deposit at 0x7ff2a8a1de40


# Account.deposit (accessed off the class) is just a plain function. It knows nothing about any specific account.
# acc1.deposit (accessed off the instance) is a bound method — Python says so right there in the output: "bound method ... of <that specific Account object>". The moment you write acc1.deposit, Python packages the function together with acc1, permanently attached, before you've even called it.


# self is what lets one single function definition correctly serve an unlimited number of different instances — each call, it just points at whichever instance is asking


# __new__ allocates the object — and that object already comes with an empty dict built in, ready to hold attributes.
# That object gets bound to self inside __init__.
# Each self.attr = value line adds one more key into that already-existing dict.
# self.owner and self.balance — yes, both go into the same dict, because they're both being set on the same self (the same instance).
# A different instance → a completely different object → a completely different (also-empty-at-first) dict. Correct

# Default parameter values in __init__

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc1 = Account("Kavya")
acc2 = Account("Rahul", 500)

print("acc1:", acc1.owner, acc1.balance)
print("acc2:", acc2.owner, acc2.balance)



class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc1 = Account("Kavya", 100)
acc2 = Account("Rahul", 500)
acc3 = Account("Priya")          # uses the default balance

for acc in (acc1, acc2, acc3):
    print(acc.owner, "-> balance:", acc.balance, "| id:", id(acc))

# Defining the class vs. instantiating it

class Account:
    print("Defining the Account blueprint...")   # not inside any method

    def __init__(self, owner, balance=0):
        print(f"Instantiating one Account for {owner}")
        self.owner = owner
        self.balance = balance

print("---")
acc1 = Account("Kavya", 100)
acc2 = Account("Rahul", 500)

# Output
# Defining the Account blueprint...
# ---
# Instantiating one Account for Kavya
# Instantiating one Account for Rahul

# Defining the class = happens once, when Python executes the class Account: block. This is where the structure gets described — what attributes exist, what methods exist.
# Instantiating = happens every time you write Account(...), however many times you want. Each call builds one new, separate, independent object from that same blueprint.