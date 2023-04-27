#Utilizando apenas lista, faça um programa que solicita a entrada de
#quatro nomes de alunos, monte uma lista e escolha aleatoriamente
#um desses nomes. A saída será a impressão do nome escolhido

import random

pessoas = []

for i in range (4):
    nome = input ('Digite o nome da pessoa: ')
    pessoas.append(nome)

print(f'A pessoa escolhida é: {random.choice(pessoas)}')
