import math

r = int(input())
if r >= 0:
    print(f"Circumference: {round(2*math.pi*r, 2)} \nArea: {round(math.pi*(r**2),2)}")
