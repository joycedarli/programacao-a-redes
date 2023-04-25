valores =[]

while True:
    valor = input("Digite um numero ou 'FIM' para terminar: " )
    if valor == 'FIM':
        break
    valor_numerico = int(valor)
    valores.append(valor_numerico)
    valores_triplo = (3* i for i in valores)
print(valores)
print(valores_triplo)
