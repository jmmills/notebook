# adapted from docs.python.org

def greet(name):
    print "Hello, number {0}!".format(name)
print "Enter a number: "
name = raw_input()
greet(name)

if int(name) <> 1:
    print 'Sorry-the number should be 1'
else:
    print 'You guessed correctly.'
