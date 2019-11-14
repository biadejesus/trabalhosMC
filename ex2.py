import math

def reduc(x):
    return x/(2**klinha)

def l(x):
    return math.log2(x)

def f(x):
    return math.factorial(x)

def ieee(x):
    if x>=0:
        e = int(l(x))
        m = 2**(l(x) - e) -1
        return m, e
    else:
        e = int(l(-x))
        m = 2**(l(-x) -e) -1
        return m, e

def raizSerie(x):
    serie = 0
    for i in range(100):
        serie = serie + ((((-1)**i) * f(2*i)) / ((1-2*i) * (f(i)**2) * (4**i))) * x**i
    return serie

x = int(input())

klinha = math.ceil(l(x))
y2 = reduc(x) - 1
raizy = 2**(klinha/2) * raizSerie(y2)

k = ieee(x)[1] 
x2 = ieee(x)[0] 
raiz = 2**(k/2.0) * raizSerie(x2)
r = math.sqrt(x)

print("pela serie: ", raizy)
print("pelo padrão ieee: ", raiz)
print("pelo python: ", r)