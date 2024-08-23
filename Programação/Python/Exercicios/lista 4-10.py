#Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
#valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
#depois, os números impares. Mostre o vetor antes de depois da modificação

vetor = []
for i in range(10):
    numero = int(input("Digite um número inteiro positivo: "))
    while numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
        numero = int(input("Digite um número inteiro positivo: "))
    vetor.append(numero)

pares = [num for num in vetor if num % 2 == 0]
impares = [num for num in vetor if num % 2 != 0]

vetor_modificado = pares + impares

print("Vetor antes da modificação:", vetor)
print("Vetor depois da modificação:", vetor_modificado)
