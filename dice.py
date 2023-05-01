import random

n = input()
while n != "q":
    n = input()
    if n == "1":
        print("Result: ", random.randint(1, 6))
    else:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(f"{a},{b} sum = {a + b}")
