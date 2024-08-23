def calcular_valor_em_reais(codigo_moeda, montante):
    cotacao_dolar = 4.98
    cotacao_libra = 6.33
    cotacao_euro = 5.42

    if codigo_moeda == 'dolar':
        valor_em_reais = montante * cotacao_dolar
    elif codigo_moeda == 'libra':
        valor_em_reais = montante * cotacao_libra
    elif codigo_moeda == 'euro':
        valor_em_reais = montante * cotacao_euro
    else:
        return "Código de moeda inválido."

    if valor_em_reais < 1000:
        comissao = valor_em_reais * 0.05
    else:
        comissao = valor_em_reais * 0.03

    total_em_reais = valor_em_reais + comissao
    return total_em_reais


codigo_moeda = input("Digite o código da moeda (dolar, libra ou euro): ")
montante = float(input("Digite o montante que deseja adquirir: "))

total_em_reais = calcular_valor_em_reais(codigo_moeda, montante)
print("Total a pagar em reais: R$", total_em_reais)