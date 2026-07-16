# class is a blueprint, it describes what something will have and will be able to do

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

acc1 = Account("Kavya", 100)

acc2 = Account("Mayur", 75)

print("acc1 itself:", acc1)
print("acc1.owner:", acc1.owner)
print("acc1.balance:", acc1.balance)
print("id(acc1):", id(acc1))

# acc1 itself: <__main__.Account object at 0x104c80590>
# acc1.owner: Kavya
# acc1.balance: 100
# id(acc1): 4375184784

print("acc2 itself:", acc2)
print("acc2.owner:", acc2.owner)
print("acc2.balance:", acc2.balance)
print("id(acc2):", id(acc2))

# acc2 itself: <__main__.Account object at 0x104c60550>
# acc2.owner: Mayur
# acc2.balance: 75
# id(acc2): 4375053648
