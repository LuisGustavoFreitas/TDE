produtos = [
    {"id": 1, "nome": "Coca-cola", "preco": 3.75, "estoque": 2},
    {"id": 2, "nome": "Pepsi", "preco": 3.67, "estoque": 5},
    {"id": 3, "nome": "Monster", "preco": 9.96, "estoque": 1},
    {"id": 4, "nome": "Café", "preco": 1.25, "estoque": 100},
    {"id": 5, "nome": "Redbull", "preco": 13.99, "estoque": 2},
]#estoque 

caixa = {
    100: 5,  # 5 notas de R$ 100
    50: 5,   # 5 notas de R$ 50
    20: 10,  # 10 notas de R$ 20
    10: 10,  # 10 notas de R$ 10
    5: 20,   # 20 notas de R$ 5
    2: 50,   # 50 notas de R$ 2
    1: 100,  # 100 moedas de R$ 1
    0.5: 200,   # 200 moedas de 50 centavos
    0.25: 200,  # 200 moedas de 25 centavos
    0.1: 500,   # 500 moedas de 10 centavos
    0.05: 1000, # 1000 moedas de 5 centavos
    0.01: 1000  # 1000 moedas de 1 centavo
} #isso é um dicionario caixa

def listarProdutos(): #essa funçao serve para defenir os produtos disponiveis
    print("Produtos disponíveis:")
    for produto in produtos:
        print(f"ID: {produto['id']} - {produto['nome']} - R$ {produto['preco']:.2f} - Estoque: {produto['estoque']}")
    print()

def encontrarProduto(idProduto): #funcao para encontrar o produto, caso nao tenha o produto 
    for produto in produtos:
        if produto["id"] == idProduto:
            return produto
    return None

def calcularTroco(valorRecebido, valorProduto): #funcao para calcular o troco 
    troco = valorRecebido - valorProduto
    if troco < 0:
        return None, troco

    trocoDistribuicao = {}
    for moeda in sorted(caixa.keys(), reverse=True):  #'sorted(caixa.keys(), reverse=True)' obtem todas as chaves do dicionario caixa e ordena em ordem decrescente
        quantidade = 0                                #'for moeda in...' do maior para o menor     
        while troco >= moeda and caixa[moeda] > 0:
            troco -= moeda #subtrai o valor restante do troco 
            troco = round(troco, 2)  # arredonda o valor do troco
            caixa[moeda] -= 1 #diminui a qntd de moeda no caixa
            quantidade += 1

        if quantidade > 0:
            trocoDistribuicao[moeda] = quantidade

    if troco > 0:
        #se nao for possivel fornecer troco exato
        for moeda, quantidade in trocoDistribuicao.items():
            caixa[moeda] += quantidade
        return None, troco

    return trocoDistribuicao, 0

def modoAdm():
    while True:
        print("\nModo Administrador")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Sair do modo administrador")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            idProduto = int(input("ID do produto: "))
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            estoque = int(input("Estoque do produto: "))
            produtos.append({"id": idProduto, "nome": nome, "preco": preco, "estoque": estoque})
            print("Produto adicionado com sucesso!")

        elif opcao == 2:
            idProduto = int(input("ID do produto a ser removido: "))
            produto = encontrarProduto(idProduto)
            if produto:
                produtos.remove(produto)
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado.")

        elif opcao == 3:
            print("Saindo do modo administrador...")
            break

        else:
            print("Opção inválida.")
            
def main():
    while True:
        listarProdutos()
        print("Digite 'admin' para entrar no modo administrador.")
        escolha = input("Escolha o ID do produto que deseja comprar: ")

        if escolha.lower() == 'admin':
            modoAdm()
            continue

        try:
            idProduto = int(escolha) #o usuario precisa digitar o ID certo
        except ValueError:
            print("ID inválido. Tente novamente.")
            continue

        produto = encontrarProduto(idProduto) #encontrar o produto no estoque
        if not produto:
            print("Produto não encontrado. Tente novamente.")
            continue

        if produto["estoque"] <= 0:
            print("Produto fora de estoque. Escolha outro produto.")
            continue

        print(f"Você escolheu {produto['nome']} - R$ {produto['preco']:.2f}")
        valorPago = float(input("Insira o valor pago: R$ "))
        troco = calcularTroco(valorPago, produto["preco"]) #calcular o troco conforme a entrada do usuario 

        if troco is None: #significa que o valor pago foi insuficiente ou não há troco disponível, o programa informa ao usuario o valor faltante      
            print(f"Valor insuficiente ou troco não disponível. Faltam R$ {abs(troco):.2f}") # 'abs()' Garantir que a mensagem exiba o valor faltante como um número positivo
            continue                                                                         # 'falta' representa a qntd de dinheiro que falta para completar o pagamento
        produto["estoque"] -= 1 #atualiza o estoque 
        print("Compra realizada com sucesso!")
        if troco: #verifica se ha troco a ser devolvido
            print("Seu troco:")
            for moeda, quantidade in troco.items(): #repete sobre cada denominaçao e quantidade de troco, exibindo a quantidade detalhada de moedas e notas a serem devolvidas 
                tipo = "moeda" if moeda < 1 else "nota"
                print(f"{quantidade} {tipo}(s) de R$ {moeda:.2f}")

main()