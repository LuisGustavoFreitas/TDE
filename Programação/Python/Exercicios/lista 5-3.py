'''Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados '''

import random

def preencherMatriz():
    matriz = []
    numerosUsados = set() 
    for i in range(4):
        linha = []
        for j in range(4):
            while True:
                numero = random.randint(100, 999)  
                if numero not in numerosUsados:  
                    numerosUsados.add(numero)  
                    linha.append(numero)
                    break
        matriz.append(linha)
    return matriz

def encontrarMaiorElemento(matriz):
    maior = matriz[0][0]
    posicaoMaior = (0, 0)
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                posicaoMaior = (i, j)
    return maior, posicaoMaior

def encontrarMenorValorLinha(matriz, linha):
    menor = matriz[linha][0]
    for elemento in matriz[linha]:
        if elemento < menor:
            menor = elemento
    return menor

def main():
    matriz = preencherMatriz()
    maior, (linhaMaior, _) = encontrarMaiorElemento(matriz)
    menorLinha = encontrarMenorValorLinha(matriz, linhaMaior)
    
    print("Matriz:")
    for linha in matriz:
        print(linha)
    
    print("\nMaior elemento da matriz:", maior)
    print("Menor elemento na linha do maior elemento:", menorLinha)

main()
