def count(n):
    if n == 0:
        print("Boom!")
    else:
        print(n)
        count(n - 1)


count(3)
