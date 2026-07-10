
# open()

# 'w' (write) — creates the file if it doesn't exist; 
# if it does exist, it truncates it (wipes contents) first. 
# So your open('demo.txt', 'w') created demo.txt because it didn't already exist.

f = open('demo.txt', 'w')
print(type(f))
print(f)
f.close()

f = open('demo.txt', 'w')
f.write('original content')
f.write('adding some content')
f.close()
print(open('demo.txt').read())          # original content

f = open('demo.txt', 'w')                # opened again with 'w'
f.write('new content\n'"Hi My name is kavya")
f.close()
print(open('demo.txt').read())          # new content — the old text is just gone

# 'r' (read) — only opens an existing file; if it doesn't exist, raises FileNotFoundError. Never creates.

# read() reads the file's contents and returns them as one big string (in text mode).
f = open('demo.txt', 'r')
print(f.read(2))
print(f.read(2))
print(f.read(2))
print(f.readline())
print(f.readline())

# It reads from the file's current cursor position, not always from the start. If you've already read part of the file (or written to it), the cursor has moved, and .read() continues from there.

f = open('demo.txt')
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()

# 'a' (append) on the same setup

f = open('demo.txt', 'w')
f.write('original content')
f.close()

f = open('demo.txt', 'a')                # 'a' this time, not 'w'
f.write(' + appended content')
f.close()

print(open('demo.txt').read())

# 'x' (exclusive creation)

# 'x' is the safety mode — it only succeeds if the file does not already exist. Useful when accidentally overwriting something would be a real problem (e.g. writing a config file you never want silently replaced).
f = open('demo.txt', 'x')
f.write('brand new file')
f.close()
print('first x worked, file created')

# try:
#     f2 = open('demo.txt', 'x')
# except FileExistsError as e:
#     print('second x failed:', e)

# 'r+' — read and write on the same file, no truncation. Rare, mostly for editing a file in place.
# 'b' suffix ('rb', 'wb') — same modes, but for binary data (images, PDFs, model weights) instead of text.

# demo.txt currently contains: "Hello World"

f = open('demo.txt', 'r+')
print(f.read())        # "Hello World"  (cursor now at end)

f.seek(0)               # move cursor back to the start
f.write('Howdy')        # overwrites first 5 chars only
f.close()

print(open('demo.txt').read())
# "Howdy World"   <- "Hello" became "Howdy", rest untouched


# demo.txt: "Hello World"
f = open('demo.txt', 'r+')
f.seek(0)
f.write('Hi')            # only 2 chars
f.close()

print(open('demo.txt').read())
# "Hillo World"   <- "Hi" overwrote "He", rest ("llo World") stays as-is


# That's the main trap with 'r+': it's overwrite-in-place, not insert/replace-the-whole-line. If you want to fully replace content cleanly, 'w' (truncate first) is usually simpler; 'r+' is for precise in-place edits when you know exact byte/character positions.

# If no f.close()

# Writes may not actually reach the disk (the big one). 
# Python/OS buffer output for performance — data you .write() often sits in a memory buffer, 
# not the actual file, until it's flushed. .close() triggers that flush. So if your program crashes or ends abnormally before closing, your written data might be lost or incomplete on disk even though .write() "succeeded" in your code

# The + is what unlocks the "other" operation. So 'r+' isn't read-only — it's read and write on an existing file (no truncate). 'w+' is also read and write, but it truncates/creates first. The base letter (r/w/a) decides how the file is initially opened (existing-only vs create vs truncate vs append-position), and + decides whether both operations are permitted.