import sys

print('Hello World!')
a = sys.argv[1]
print('a = ' + a)
b = input('Gimme something!  ')
print(b)

a = 0
b = 1
a = a + 1
b = b + 1
print(f'values = {(a, b)}')
a = a + 1
b = b + 1
print(f'values = {(a, b)}')
a = a + 1
b = b + 1
print(f'values = {(a, b)}')



