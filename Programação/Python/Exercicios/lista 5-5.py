'''Escreva um programa que popule uma matriz (15 x 7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação'''

import random

def criarMatriz():
    matriz = []
    for i in range(15):
        linha = [random.randint(10, 99) for _ in range(7)]
        matriz.append(linha)
    return matriz

def mostrarMatriz(matriz):
    for linha in matriz:
        print(' '.join(map(str, linha)))
    print()

def modificarMatriz(matriz):
    elementos = [num for linha in matriz for num in linha]
    pares = [num for num in elementos if num % 2 == 0]
    impares = [num for num in elementos if num % 2 != 0]
    novaLista = pares + impares
    
    novaMatriz = []
    for i in range(15):
        linha = novaLista[i*7:(i+1)*7]
        novaMatriz.append(linha)
    
    return novaMatriz

matrizOriginal = criarMatriz()

print("Matriz Original:")
mostrarMatriz(matrizOriginal)

matrizModificada = modificarMatriz(matrizOriginal)

print("Matriz Modificada:")
mostrarMatriz(matrizModificada)
