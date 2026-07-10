with open('demo.txt', 'w') as f:
    f.write('hello')
print(f.closed)

# The moment the indented block under with ends, Python closes the file for you automatically. f is still a valid variable outside the block (that's why f.closed works), it's just that the connection is now shut.
import os 

with open('demo.txt', 'w') as f:
    f.write('some important data')
    print('size on disk INSIDE the with block:', os.path.getsize('demo.txt'))

print('size on disk AFTER the with block:', os.path.getsize('demo.txt'))

# Fix for problem #2 (running out of file handles)
for i in range(2000):
    with open(f'/tmp/file_{i}.txt', 'w') as f:
        f.write('x')
print('all 2000 files done, no crash')

# Output:
# all 2000 files done, no crash