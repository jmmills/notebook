import math

phi = (1 + math.sqrt(5)) / 2

def fib(n):
    if n < 2:
        return n

    return round( (phi ** n - (1 - phi) ** n) / math.sqrt(5) )

if __name__ == '__main__':
    place = 2 ** 5
    print(fib(place))
