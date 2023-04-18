massa = int(input('Digite seu peso: '))
altura = int(input('Digite sua altura: '))

imc = massa/ (altura  * altura)

if imc<18.5:
    print("Abaixo do peso.", imc)

elif imc>=18.5 and imc <25:
    print("Peso normal.")

elif imc >=25 and imc<30:
    print("sobrepeso.")