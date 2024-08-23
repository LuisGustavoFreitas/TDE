#Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar

#Entrada
n =float(input("Digite um número:"))
resto=n%2

#Desenvolvimento
if resto == 0:
    print('O número é par!!!')
else:
    print('O número é impar!!!')