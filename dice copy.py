import random

a = [0] * 12
for i in range(10000):
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    a[x + y - 1] += 1
print(*a)
