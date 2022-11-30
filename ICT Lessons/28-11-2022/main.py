n = int(input())
l = list(map(int, input().split()))
q = int(input())
for _ in range(q):

    query = list(map(int, input().split()))
    if query[0] == 1:
        l.append(0)
        for i in range(len(l) - 1, query[1], -1):
            l[i] = l[i - 1]
        l[query[1]] = query[2]

    if query[0] == 2:
        del l[query[1]]
print(len(l))
print(*l)
