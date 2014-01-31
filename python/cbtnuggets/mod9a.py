#!/usr/bin/python3

S = [ x ** 2 for x in range(10) ]

def choice_a(x):
    print(S)
    return

def choice_b(x):
    V = [ 2 ** i for i in range (x) ]
    print(V)
    return

def choice_c(y):
    M = [ x for x in range(y) if x % 2 == 0 ]
    print(M)

def choice_d():
    raise SystemExit

print ('Which operation do you want to perform?\n')
print('''
a: x to the second power
b: 2 the xth power
c: mod 2
d: quit program
''')

resp = input('Choice: ')
resp2 = int(input('Upper limit? '))

if resp == 'a':
    choice_a(resp2)
elif resp == 'b':
    choice_b(resp2)
elif resp == 'c':
    choice_c(resp2)
else:
    choice_d()
