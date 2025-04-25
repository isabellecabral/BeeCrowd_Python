try:
    aux = input('Digite suas 4 notas').split()
    n1 = float(aux[0])
    n2 = float(aux[1])
    n3 = float(aux[2])
    n4 = float(aux[3])

    if n1 <0 or n2 <0 or n3 <0 or n4 <0:
        print('Digite um valor positivo')
    elif n1>10 or n2>10 or n3>10 or n4>10:
        print('Digite um valor menor ou igual a 10')
    else:
        media = (n1*2 + n2*3 + n3*4 + n4*1)/10
        print(f'Média: {media}')
        if media<5:
            print('Reprovado')
        elif media<=6.9:
            print('Aluno em Exame')

            try:
                ntexame = float(input('Digite sua nota de exame: '))
                print(f'Nota de exame: {ntexame}')
                mediaexame = (ntexame + media)/2
                if mediaexame<5:
                     print('Reprovado')
                     print (f'Média final: {mediaexame}')
                else:
                    print('Aluno Aprovado')
                print (f'Média final: {mediaexame}')
            except(ValueError, TypeError):
                print('Digite um valor númerico para a média do exame')

        else:
            print('Aprovado de primeira')

except(ValueError, IndexError):
    print('Digite um valor correto para as notas')







