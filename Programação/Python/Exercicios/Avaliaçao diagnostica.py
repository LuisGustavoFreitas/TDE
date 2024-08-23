def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

quantidade = int(input("Digite a quantidade de números a serem inseridos: "))
numeros_pares = 0
numeros_impares = 0
numeros_primos = 0
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: : "))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    if primo(numero):
        numeros_primos += 1
print("Quantidade de números pares:", numeros_pares)
print("Quantidade de números ímpares:", numeros_impares)
print("Quantidade de números primos:", numeros_primos)

