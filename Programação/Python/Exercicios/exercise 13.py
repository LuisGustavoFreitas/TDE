#Entrada
produtoPreco = float(input("Informe o preço do produto: R$ " ))
print("O preço do produto é: R$ {}".format(produtoPreco))
print("""
[1] - À vista com 8% de desconto
[2] - 2x mais 4% de desconto
[3] - 3x no cartão 
[4] - 4x mais 4% de juros
""")
opcaoPagamento = int(input("Informe a opção de pagamento:"))

#Desenvolvimento
if opcaoPagamento == 1:
    precoAtualizado = produtoPreco - (produtoPreco * 0.08)
    print("O preço atual é: R${}".format(precoAtualizado))
if opcaoPagamento == 2:
    precoAtualizado = (produtoPreco - produtoPreco * 0.04) / 2
    print("O preço atual é: R${}".format(precoAtualizado))
if opcaoPagamento == 3:
    precoAtualizado = produtoPreco / 3
    print("O preço atual é: R${}".format(precoAtualizado))
if opcaoPagamento == 4:
    precoAtualizado = (produtoPreco  + produtoPreco * 0.04) / 4
    print("O preço atual é: R${}".format(precoAtualizado))