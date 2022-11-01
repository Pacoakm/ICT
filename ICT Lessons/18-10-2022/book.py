a, b, c = map(int, input().split())
s = a*0.2 + b*0.3 + c*0.5
if s >= 90:
    print("A")
elif 80<=s<90:
    print("B")
elif 