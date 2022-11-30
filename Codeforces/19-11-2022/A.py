n, k = map(int, input().split())
b = list(map(int, input().split()))
min = 1e18 + 1
x = 0
for i in range(k):
    if n % b[i] < min:
        min = n % b[i]
        x = i

print(f"{x+1} {n//b[x]}")
