
print("="*20)
print("     COMPRAS")
print("="*20)
print()
produtoPreco = float(input("Informe o preço do produto: R$"))
print("O preço do produto é:{}".format(produtoPreco))
print("""
[1] - À vista dinheiro/cheque: 5% de desconto
[2] - Em até 2X no cartão: preço normal
[3] - 3x ou mais no cartão: 5% de juros""")
opcaoPagamento = int(input("Informe a opção de pagamento:"))
if opcaoPagamento == 1:
    precoAtualizado = produtoPreco - (produtoPreco*0.05)
    print("O preço atual é: R${}".format(precoAtualizado))
elif opcaoPagamento == 2:
    precoAtualizado = produtoPreco - (produtoPreco*0.5)
    print("O preço atual é: R${}".format(precoAtualizado))
elif opcaoPagamento == 3:
    precoAtualizado = produtoPreco + (produtoPreco*0.2)
    print("O preço atual é: R${}".format(precoAtualizado))