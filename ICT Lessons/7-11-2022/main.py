n = int(input())
l = list(map(int, input().split()))
c = 0
for i in range(n):
    if l[i + 1] >= l[i]:
        c = c + 1
if c == n - 1:
    print("Yes")
else:
    print("No")
