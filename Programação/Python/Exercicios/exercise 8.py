#Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo
#praticado. Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. Elabore um
#algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no
#estacionamento e mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado, R$
#x”, no qual x será o valor a pagar calculado pelo algoritmo.

#Entrada
tempo=int(input('Quanto tempo você ficou em minutos:'))

#Desenvolvimento
preco=((tempo/15)*1.50)+8
if tempo<=60:
    print("O valor a pagar é: R$ 8.00")
if tempo>60:
    preco=(((tempo-60)//15)*1.50)+8
    if (tempo-60) % 15 != 0:
        preco+= 1.50
    print("O valor a pagar é: R$ {} ".format(preco))
