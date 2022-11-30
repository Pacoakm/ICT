a, b = map(int, input().split())
for i in range(1, a + 1):
    if i == 1 or i == a:
        print("*" * b)
    else:
        print("*" + " " * b - 2 + "*")
