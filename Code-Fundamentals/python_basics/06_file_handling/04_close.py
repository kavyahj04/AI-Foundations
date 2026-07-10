# Problem #1 — your data might not actually be on disk yet

import os

f = open('demo.txt', 'w')
f.write('some important data')
# NOT closed yet
print('size on disk before close:', os.path.getsize('demo.txt'))
f.close()
print('size on disk after close:', os.path.getsize('demo.txt'))

# Python doesn't push every .write() straight to the hard drive; it holds recently written data in a memory buffer for efficiency, and only actually commits it to disk when the buffer fills up, or when you close the file. So: if your program crashed right after that .write() but before .close(), that data would be gone — it never made it past RAM.

# Problem #2 — the operating system has a hard limit on open files

files = []
for i in range(2000):
    f = open(f'/tmp/file_{i}.txt', 'w')
    files.append(f)
    # never closing any of them

# crashed after opening 1021 files
# error: [Errno 24] Too many open files: '/tmp/file_1021.txt'
# Real crash, real error. Every open file handle is a limited OS resource (this machine caps it at 1024). If your code opens files in a loop — say, processing a folder of 5,000 log files — and forgets to close each one before moving to the next, you will eventually hit this exact error and your program dies.

