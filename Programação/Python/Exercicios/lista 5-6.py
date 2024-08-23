'''A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. Para
consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e
São Paulo é de 408 km. Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima
e que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas.'''

distancias = [
    [0, 310, 716, 408, 852],   # Curitiba
    [310, 0, 470, 705, 1144],  # Florianopolis
    [716, 470, 0, 1119, 1553], # Porto Alegre
    [408, 705, 1119, 0, 429],  # Sao Paulo
    [852, 1144, 1553, 429, 0]  # Rio de Janeiro
]

cidades = {
    "Curitiba": 0,
    "Florianopolis": 1,
    "Porto Alegre": 2,
    "Sao Paulo": 3,
    "Rio de Janeiro": 4
}

def calcularTempo(distancia, velocidadeMedia=80):
    return distancia / velocidadeMedia

def main():
    print("Cidades disponíveis: Curitiba, Florianopolis, Porto Alegre, Sao Paulo, Rio de Janeiro")
    
    cidadeOrigem = input("Digite a cidade de origem: ")
    cidadeDestino = input("Digite a cidade de destino: ")
    
    if cidadeOrigem not in cidades or cidadeDestino not in cidades:
        print("Cidades inválidas. Por favor, tente novamente.")
        return
    
    origem = cidades[cidadeOrigem]
    destino = cidades[cidadeDestino]
    
    distancia = distancias[origem][destino]
    
    if distancia == 0:
        print(f"A distância entre {cidadeOrigem} e {cidadeDestino} não é aplicável.")
    else:
        tempo = calcularTempo(distancia)
        print(f"A distância entre {cidadeOrigem} e {cidadeDestino} é de {distancia} km.")
        print(f"O tempo estimado de viagem a uma velocidade média de 80 km/h é de {tempo:.2f} horas.")
main()