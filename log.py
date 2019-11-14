import math

def logn(x):
    sinal = 1
    serie = 0
    for i in range (1,100):
        serie += sinal * ((x**i)/i)
        sinal *= -1
    return serie

def reducao(x):
    return x/(2**(k))

x = int (input())

k = math.ceil(math.log2(x))

xlinha = reducao(x) -1
ln = logn(xlinha) + k*(math.log(2))
print("calculado: ", ln)
print("Python: ", math.log(x))