fizz = lambda x: x % 3 == 0 
buzz = lambda x: x % 5 == 0
fizzbuzz = lambda x: fizz(x) and buzz(x)

def showme(n, v):
    print("{0}: {1}".format(n, v))

for n in range(1, 100):
  if fizzbuzz(n):
    showme(n, 'FizzBuzz')
  elif fizz(n):
    showme(n, 'Fizz')
  elif buzz(n):
    showme(n, 'Buzz')
