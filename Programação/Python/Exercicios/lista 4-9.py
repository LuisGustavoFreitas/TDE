#Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
#Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
#contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
#zeros. Mostre então os três vetores.

vLido = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vLido.append(numero)

vPares = [num for num in vLido if num % 2 == 0 and num != 0]
vImpares = [num for num in vLido if num % 2 != 0 and num != 0]

print("vLido:", vLido)
print("vPares:", vPares)
print("vImpares:", vImpares)
