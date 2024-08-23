#Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
#“Valor inválido” para números negativos)

import math
#Entrada
numero=int(input("Digite um número:"))

#Desenvolvimento
if numero < 0:
    print("Número invalido")
else:
    raiz=math.sqrt(numero)
    print("A raiz do número é" , raiz)