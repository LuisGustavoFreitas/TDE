'''Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5 x 5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores:'''

import random

def criarMatriz(linhas, colunas):
  matriz = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha.append(random.randint(10, 99))
    matriz.append(linha)
  return matriz

def imprimirMatriz(matriz):
  for linha in matriz:
    for elemento in linha:
      print(elemento, end=" ")
    print()

def obterAreaSombreada(matriz, linhaEsquerdaSuperior, colunaEsquerdaSuperior, linhaDireitaInferior, colunaDireitaInferior):
  areaSombreada = []
  for i in range(linhaEsquerdaSuperior, linhaDireitaInferior + 1):
    linha = []
    for j in range(colunaEsquerdaSuperior, colunaDireitaInferior + 1):
      linha.append(matriz[i][j])
    areaSombreada.append(linha)
  return areaSombreada  

def calcularSoma(matriz):
  somaTotal = 0
  for linha in matriz:
    for elemento in linha:
      somaTotal += elemento
  return somaTotal

matriz = criarMatriz(5, 5)
imprimirMatriz(matriz)

areaSombreada = obterAreaSombreada(matriz, 1, 1, 3, 3)  
imprimirMatriz(areaSombreada)

soma_areaSombreada = calcularSoma(areaSombreada)
print("Soma da área sombreada:", soma_areaSombreada)
