'''
aux = input('Digite o número da comida desejada').split()
op = int(aux[0])
qt = int(aux[1])

if op == 1:
    preco = 4
elif op == 2:
    preco = 4.5
elif op == 3:
    preco = 5
elif op == 4:
    preco = 2
elif op == 5:
    preco = 1.5
else:
    preco = 0

if preco ==0:
    print('Opção Inválida')
else:
    resultado = preco * qt
    print(resultado)

'''

#Versão Melhorada

precos ={
    1: 4,
    2: 4.5,
    3: 5,
    4:2,
    5:1.5
}

try:
    aux = input('Digite o número da comida desejada e sua quantidade:').split()
    op = int(aux[0])
    qt = int(aux[1])

    if op in precos:
        resultado = precos[op] * qt
        print(resultado)
    else:
        print('Opção Inválida')
except(IndexError, ValueError):
    print('Entrada Inválida. Digite dois numeros separados por espaço')