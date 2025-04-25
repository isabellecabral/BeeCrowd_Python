num= float(input('Digite um valor'))

if num<0:
    print('Fora do intevalo')
elif num <=25:
    print('Intervalo [0,25]')
elif num <=50:
    print('Intervalo (25,50]')
elif num <=75:
    print('Intervalo (50,75]')
elif num <=100:
    print('Intervalo (75,100]')
else:
    print('Fora do intervalo')