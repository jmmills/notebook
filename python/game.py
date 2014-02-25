import random

words_used = ["python", "compiler", "perl","javascript"]
another = ["a","b","c","d"]
tisk = list(another)
tisk.reverse()

def pop_one(a):
    if len(a) == 0:
        return False

    i = random.choice(a)
    print(i)
    a.remove(i)

    return True


while pop_one(words_used):
    pass

print('---')

while pop_one(another):
    pass

print('---')
for i in range(3):
    pop_one(tisk)


print(tisk)