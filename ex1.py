import math

aux = math.log(2)/512

def f(x):
    return math.factorial(x)

def erroM():
    return aux**5/f(5)

def acharR(x):
    n = math.ceil((256 * aux-x) / (-math.log(2)))
    r = (x - (n * math.log(2))) / 256
    return r, n

def serieR(r, n):
    return 2**n * (((((((((1+r*(1+r*(1/f(2)+r*(1/f(3)+r*1/f(4)))))**2)**2)**2)**2)**2)**2)**2)**2)

def serie(r, n):
    res = 0
    for i in range(4):
        res += r**i/f(i)
    return (2**n) * (res**256)

x = int(input())

r, n = acharR(x)

serieR = serieR(r, n)
serie = serie(r, n)
exp = math.e**x

print("Serie Reduzida: ", serieR)
print("Serie normal: ", serie)
print("Biblioteca do Python: ", exp)