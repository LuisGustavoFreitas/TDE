produtoPreco = float(input("Informe o preço do produto: R$"))
print("O preço do produto é:{}".format(produtoPreco))
print("""
[1] - À vista com 5% de desconto
[2] - Em até 2X no cartão
[3] - 3x no cartão mais 5% de juros
""")
opcaoPagamento = int(input("Informe a opção de pagamento:"))
if opcaoPagamento == 1:
    precoAtualizado = produtoPreco - (produtoPreco*0.05)
    print("O preço atual é: R${}".format(precoAtualizado))
if opcaoPagamento == 2:
    precoAtualizado = produtoPreco - (produtoPreco*0.5)
    print("O preço atual é: R${}".format(precoAtualizado))
if opcaoPagamento == 3:
    precoAtualizado = (produtoPreco + produtoPreco * 0.05) / 3
    print("O preco atual é: R$ {}" . format(precoAtualizado))