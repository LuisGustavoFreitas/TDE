'''Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4 x 4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.'''

def main():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
            linha.append(valor)
        matriz.append(linha)
    vetor = [None] * 4

    for j in range(4):
        maior_valor = matriz[0][j]
        for i in range(1, 4):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
        vetor[j] = maior_valor

    media = sum(vetor) / len(vetor)

    print("Matriz:")
    for linha in matriz:
        print(linha)

    print("Vetor dos maiores valores de cada coluna:")
    print(vetor)

    print("Média aritmética do vetor:")
    print(media)

main()
