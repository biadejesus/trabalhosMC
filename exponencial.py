import math

def f(x):
    return math.factorial(x)

def exponencial(x):
    serie = 0
    for i in range (17):
        serie += ((x**i)/(f(i)))
    return 2**k * serie

x = float(input())
c = math.log(2,math.e)
k = math.ceil((c - x) / (- c))
xlinha = x - k * c #redução aditiva


calc = str(exponencial(xlinha))

real = str(math.exp(x))

print("Exponencial calculado:", calc)
print("Exponencial python:", real)