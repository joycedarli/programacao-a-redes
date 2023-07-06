n = int(input('Digite um numero de 0 a 9999:'))

unidade = n % 9999
n = (n - unidade)/ 9999
dezena = n % 9999
n = (n - dezena)/ 9999
centena = n

dezena = (int(dezena))
centena = (int(centena))

print(centena, dezena, unidade)