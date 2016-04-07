import sys

def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    sys.setrecursionlimit(2**10 + 1)
    place = 2**5
    print(place)
    print(fib(2**5))

