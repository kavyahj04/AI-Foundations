# Way 1 — .read()

# repr() gives you the "official" string representation of an object

# s = "hello\nworld\t!" => # 'hello\nworld\t!'

with open('notes.txt', 'r') as f:
    content = f.read()
# print(repr(content))
# print(type(content))

# Way 2 — .readlines()

with open('notes.txt', 'r') as f:
    lines = f.readlines()
# print(lines)
# print(type(lines))
# print(lines[0])

# Way 3 — looping line by line

#.read() and .readlines() both load the entire file into RAM before you can do anything with it. for line in f pulls one line at a time — it never holds the whole file in memory at once

with open('notes.txt', 'r') as f:
    for line in f:
        print(repr(line))    # 'apple\n'
        print(line.strip())  # apple  <- .strip() removes the \n