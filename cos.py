import math

def f(x):
    return math.factorial(x)

def r(x):
    return math.radians(x)

def seno(x):
    serie = 0
    sinal = 1
    for i in range (1,12,2):
        serie +=  sinal * (x**i/f(i))
        sinal *= -1
    return serie

def cos(x):
    serie = 0
    sinal = 1
    for i in range (0,13,2):
        serie += sinal * (x**i/f(i))
        sinal *= -1
    return serie
    
x = int (input('insira o angulo: '))

aux = x%360

if aux >= 0 and aux < 90:
    ang = aux
    sinal = 1 

elif aux >= 90 and aux < 180:
    ang = 180 - aux
    sinal = -1

elif aux >= 180 and aux < 270:
    ang = aux - 180
    sinal = -1
    
else:
    ang = 360 - aux 
    sinal = 1 

if ang <= 45:
    result = sinal * (cos(r(ang))) 
else:
    result = sinal * (seno(r(90-ang)))

print("cosseno calculado: ", result)
print("cosseno python: ", math.cos(r(aux)))
#testando um bagulho no git
