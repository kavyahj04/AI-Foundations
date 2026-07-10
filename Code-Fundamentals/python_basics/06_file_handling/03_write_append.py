# write

# .write() only accepts strings — nothing else

f = open('demo2.txt', 'w')
# f.write(42)
f.write(str(42))

# The gotcha that trips up almost everyone: .write() does NOT add a newline for you

f = open('demo2.txt', 'w')
f.write('apple')
f.write('banana')
f.close()
# print(repr(open('demo2.txt').read()))

f = open('demo2.txt', 'w')
f.write('apple\n')
f.write('banana\n')
f.close()
# print(repr(open('demo2.txt').read()))

# .writelines() — writes a list of strings in one call, same gotcha

f = open('demo3.txt', 'w')
f.writelines(['apple\n', 'banana\n', 'cherry\n'])
f.close()
print(repr(open('demo3.txt').read()))

# .write() has a return value — the number of characters written

f = open('demo.txt', 'w')
result = f.write('hello')
print(result)
