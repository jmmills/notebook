# adapted from docs.python.org

def greet(name):
    print("Hello, number {0}!".format(name))
name = input("Enter a number: ")
greet(name)

if int(name) != 1:
    print('Sorry-the number should be 1')
else:
    print('You guessed correctly.')
