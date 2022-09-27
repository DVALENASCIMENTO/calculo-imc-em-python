# Descrição: Calcular o imc e classificar de acordo com a tabela abaixo:
# Autor: Diego Vale do Nascimento - 07/09/2022

peso = float(input("informe o peso: "))
altura = float(input("informe a altura: "))

imc = peso/(altura**2)

print("imc: ", imc)

if (imc < 19.1):
    print("Abaixo do peso")

elif (imc >= 19.1 and imc < 25.8):
    print("Peso ideal")

elif (imc >= 25.8 and imc < 27.3):
    print("Um pouco acima do peso")

elif (imc >= 27.3 and 32.3):
    print("Muito acima do peso")

elif (imc >= 32.3):
    print("Obesidade")