import math

def f(x):
    return math.factorial(x)

def exponencial(x):
    c = math.log(2,math.e)
    k = math.ceil((c - x) / (- c))
    res = x - k * c
    soma = 0
    for i in range (17):
        soma += ((res**i)/(f(i)))
    
    return 2**k * soma
  
x = float(input())

inteiro, decimal = str(exponencial(x)).split('.')
calc = inteiro + '.' + decimal[:10] + '|' + decimal[10:]
intreal, decreal = str(math.Exp(x)).split('.')
real = intreal + '.' + decreal[:10] + '|' + decreal[10:]
print("Exp calc:", calc)
print("Exp real:", real)