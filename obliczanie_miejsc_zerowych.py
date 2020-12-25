from math import sqrt


def f(x, a, b, c):
    wynik = a * x * x + b * x + c
    if wynik > 0 and wynik < 0.0000000001:
        return 0
    else:
        return wynik


def oblicz_delte(a, b, c):
    return b * b - 4 * a * c

def oblicz_miejsca_zerowe(a, b, d):
    if d < 0:
        print("nie umiem tego obliczyć")
    elif d == 0:
        return -b / 2
    else:
        return (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)


a = 2
b = 0
c = 4
delta = oblicz_delte(a, b, c)
print(delta)
try:
    x1, x2 = oblicz_miejsca_zerowe(a, b, delta)

    print(x1, x2)
    print(f(x1, a, b, c), f(x2, a, b, c))

except TypeError:
    x1 = oblicz_miejsca_zerowe(a, b, delta)
    x2 = x1
    if type(x1) == int or type(x1) == float:
        print(x1, x2)
        print(f(x1, a, b, c), f(x2, a, b, c))