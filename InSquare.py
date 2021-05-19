""" a = input()
s = a.split(".")
x = int(s[0])
if int(s[1][0]) >= 5:
    x += 1
print(x) """


def IsPointInCircle(x, y, xc, yc, r):
        return ((x + xc)**2 + (y + yc)**2) <= r**2


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
elif not IsPointInCircle(x, y, xc, yc, r):
    print('NO')
else:
    print('error')
