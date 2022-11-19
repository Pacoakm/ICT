n = int(input())
a = [0] * 11
for i in input().split():
    a[int(i)] += 1
for i in range(1, 11):
    print(f"{i}: {a[i]}")
