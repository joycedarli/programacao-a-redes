maior_valor = None

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b:
    if a > c:
        maior_valor = a
    else:
        maior_valor = c
else:
    if b > c:
        maior_valor = c 
    else:
        maior_valor = c
print("Maior valor:", maior_valor)