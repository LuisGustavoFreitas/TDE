#Ler 4 números inteiros e calcular a soma dos que forem par

def calcular_soma_pares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros = []
for i in range(4):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

soma_pares = calcular_soma_pares(numeros)

print("A soma dos números pares é:", soma_pares)
