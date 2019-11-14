import math

def f(x):
    return math.factorial(x)

def serie(x):
    res = 0
    for i in range(100):
        res = res + (((((-1)**i) * f(2*i)) / ((1-2*i) * (f(i)**2) * (4**i))) * x**i)
    return res

def reducao(x):
    return x/(2**(k))

def g(x):
    return (2**(k/2)) * (serie(reducao(x) - 1))

x = float(input())
k = math.ceil(math.log2(x))

resultado = str(g(x))
real = str(x**0.5)

print("raiz calculada: ", resultado)
print("raiz python: ", real)