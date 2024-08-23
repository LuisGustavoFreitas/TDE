#Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > (num2 + num3):
    print(f"{num1} é maior que a soma de {num2} e {num3}.")
else:
    print(f"{num1} não é maior que a soma de {num2} e {num3}.")