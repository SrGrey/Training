""" a = input()
s = a.split(".")
x = int(s[0])
if int(s[1][0]) >= 5:
    x += 1
print(x) """


def raiz(a, b, c):
    d = b**2 - 4 * a * c
    if d == 0:
        x = (- b + d**(1/2)) / (2 * a)
        print(x)
    elif d > 0:
        x1 = (- b + d**(1/2)) / (2 * a)
        x2 = (- b - d**(1/2)) / (2 * a)
        print(min(x1, x2), max(x1, x2))


a, b, c = float(input()), float(input()), float(input())
raiz(a, b, c)
