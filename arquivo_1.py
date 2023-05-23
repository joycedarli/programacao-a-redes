from asyncore import write
import email


lista_pessoas = []
while True:
    print("="*50)
    nome = input("digite o nome da pessoa: ")
    if nome == "END":
        break
    email = input("digite o email da pessoa: ")
    if email == "END":
        break
    pessoa = [nome,email]
    lista_pessoas.append(pessoa)

lista_str = []
for pessoa in lista_pessoas:
    lista_str.append(",".join(pessoa))
dado = '/n'.join(lista_str)

with open("pessoas.txt", "wt") as f:
    f.write(dado)