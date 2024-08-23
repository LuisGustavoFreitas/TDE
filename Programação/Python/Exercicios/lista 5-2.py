'''Implemente um programa que permita multiplicar uma matriz de ordem (3 x 3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.
Lembrete: para multiplicar uma matriz Am x n por um escalar k, basta multiplicar cada entrada aij
de A por k. Assim, a matriz resultante B será também da ordem (m x n) e bij = k * aij. '''

def lerMatriz():
    matriz = []
    for i in range(3):
        linha = list(map(int, input(f"Digite os 3 valores da linha {i+1} com um espaço entre eles: ").split()))
        matriz.append(linha)
    return matriz

def multiplicarMatriz(matriz, escalar):
    matrizResultante = []
    for i in range(3):
        linhaResultante = []
        for j in range(3):
            linhaResultante.append(matriz[i][j] * escalar)
        matrizResultante.append(linhaResultante)
    return matrizResultante

def main():
    print("Digite os valores da matriz 3x3:")
    matriz =lerMatriz()
    
    escalar = int(input("Digite o valor do escalar: "))
    
    matrizResultante = multiplicarMatriz(matriz, escalar)
    
    print("Matriz resultante após a multiplicação pelo escalar:")
    for linha in matrizResultante:
        print(linha)
main()