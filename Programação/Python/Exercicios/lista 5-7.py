'''Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário
informar várias cidades em sequência, até inserir um código finalizador. Mostre então as cidades que
compõem o roteiro fornecido, a distância de cada percurso intermediário e a distância total do roteiro
fornecido.'''

distancias = [
    [0, 310, 716, 408, 852],   # Curitiba
    [310, 0, 470, 705, 1144],  # Florianópolis
    [716, 470, 0, 1119, 1553], # Porto Alegre
    [408, 705, 1119, 0, 429],  # São Paulo
    [852, 1144, 1553, 429, 0]  # Rio de Janeiro
]

cidades = {
    "Curitiba": 0,
    "Florianopolis": 1,
    "Porto Alegre": 2,
    "Sao Paulo": 3,
    "Rio de Janeiro": 4
}

def calcularDistanciaTotal(roteiro):
    distanciaTotal = 0
    distanciaPercurso = []
    for i in range(len(roteiro) - 1):
        origem = cidades[roteiro[i]]
        destino = cidades[roteiro[i + 1]]
        distancia = distancias[origem][destino]
        distanciaPercurso.append(distancia)
        distanciaTotal += distancia
    return distanciaTotal, distanciaPercurso

def main():
    print("Cidades disponíveis: Curitiba, Florianopolis, Porto Alegre, Sao Paulo, Rio de Janeiro")
    print("Digite 'fim' para finalizar o roteiro.")
    
    roteiro = []
    while True:
        cidade = input("Digite o nome da cidade: ")
        if cidade.lower() == "fim":
            break
        if cidade not in cidades:
            print("Cidade inválida. Por favor, tente novamente.")
        else:
            roteiro.append(cidade)
    
    if len(roteiro) < 2:
        print("Você deve inserir pelo menos duas cidades para calcular o roteiro.")
        return
    
    distanciaTotal, distanciaPercurso = calcularDistanciaTotal(roteiro)
    
    print("Roteiro fornecido:")
    for i in range(len(roteiro) - 1):
        print(f"{roteiro[i]} -> {roteiro[i + 1]}: {distanciaPercurso[i]} km")
    
    print(f"Distância total do roteiro: {distanciaTotal} km")

main()
