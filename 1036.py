import math

dados = input("Digite o valor de a, b e c").split()
a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('Impossivel calcular')
elif a==0:
    print('Impossivel calcular')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(round(x1,5), round(x2,5))