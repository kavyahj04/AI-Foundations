print("="*70)
print("STAGE 1: what '=' actually does in Python -- no classes, no functions")
print("="*70)
a = [1, 2, 3]
b = a
print("a:", a)
print("b:", b)
b.append(4)
print("after b.append(4):")
print("a:", a, "  <- a changed too!")
print("b:", b)
print("a is b ->", a is b)
print("WHY: 'b = a' did not copy the list. It made 'b' another name")
print("pointing at the exact same list object 'a' already points at.")
print("There is only ONE list in memory here, with two names on it.")

print()
print("="*70)
print("STAGE 2: 'self.x = value' follows the EXACT same rule")
print("="*70)

class Box:
    def __init__(self, items):
        self.items = items      # same rule as b = a above

my_list = [1, 2, 3]
box1 = Box(my_list)
box1.items.append(4)
print("my_list:", my_list, "  <- changed, because box1.items IS my_list")
print("box1.items is my_list ->", box1.items is my_list)
print("self.items = items did not copy items. It made 'self.items' another")
print("name pointing at the SAME list that was passed in.")

print()
print("="*70)
print("STAGE 3: forget classes entirely -- default args are built ONCE")
print("="*70)

def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print("call 1:", add_item("a"))
print("call 2:", add_item("b"))
print("call 3:", add_item("c"))
print("Notice: each call KEEPS the previous items. 'bucket=[]' was created")
print("ONE time when 'def add_item' ran, not fresh on every call.")

print()
print("="*70)
print("STAGE 4: put both rules together -- this IS the BuggyAccount bug")
print("="*70)

class BuggyAccount:
    def __init__(self, owner, history=[]):   # this [] built ONCE  (Stage 3's rule)
        self.history = history               # self.history = history  (Stage 1/2's rule)

acc1 = BuggyAccount("Kavya")
acc2 = BuggyAccount("Rahul")
acc1.history.append("Kavya opened account")
print("acc1.history:", acc1.history)
print("acc2.history:", acc2.history, " <- same list, so it shows up here too")
print("acc1.history is acc2.history ->", acc1.history is acc2.history)