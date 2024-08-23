#Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
#número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
#posição(ões) ele foi encontrado e quantas ocorrências foram detectadas

def pesquisar_numero(vetor, numero):
    posicoes = []
    ocorrencias = 0
    for i, valor in enumerate(vetor):
        if valor == numero:
            posicoes.append(i)
            ocorrencias += 1
    return posicoes, ocorrencias

vetor = []
for i in range(10):
    numero = int(input("Digite um número inteiro para a posição {}: ".format(i)))
    vetor.append(numero)

numero_pesquisa = int(input("Digite o número que deseja pesquisar: "))
posicoes, ocorrencias = pesquisar_numero(vetor, numero_pesquisa)

if ocorrencias > 0:
    print("O número {} foi encontrado nas seguintes posições:".format(numero_pesquisa))
    for posicao in posicoes:
        print("- Posição:", posicao)
    print("Total de ocorrências:", ocorrencias)