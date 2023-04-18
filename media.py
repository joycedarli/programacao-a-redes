n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print('Media: ', media)
    
if media<7.0:
    print('Reprovado')
elif media<10:
    print('Aprovado')
elif 2.0 <= media < 7.0:
    print('Recuperação')

