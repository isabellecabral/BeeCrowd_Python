try:
    aux = input('Digite uma coordenada: ').strip("()").replace(" ", "")
    aux= aux.split(",")
    x = float(aux[0])
    y = float(aux[1])

    if x>0:
        if y>0:
            print('Quadrante 1')
        elif y<0:
            print('Quadrante 4')
        else :
            print('Eixo X')
    elif x<0:
        if y>0:
            print('Quadrante 2')
        elif y<0:
            print('Quadrante 3')
        else :
            print('Eixo X')
    else:
        if y!=0:
            print('Eixo Y')
        else:
            print('Origem')
except(ValueError, TypeError):
    print('Digite o valor corretamente, exemplo: (2, -2)')

