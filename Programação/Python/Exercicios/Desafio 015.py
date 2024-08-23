dias=int(input('Digite a quantidade de dias com o carro alugado: '))
km= float(input('Digite quantos Km rodados: '))
pago= (dias*60) + (km* 0.15)
print('O total a pagar é: R${:.2f }' . format(pago))