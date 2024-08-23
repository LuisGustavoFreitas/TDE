#Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100
#cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20. Elabore
#um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço

#Entrada
fotocopia= 0.25
fotocopia2= 0.20
quantidade= int(input("Digite quantas cópias deseja realizar: "))

#Desenvolvimento
if quantidade <=100:
    preco= quantidade * fotocopia
    print("O valor das cópias é R$ {} " .format (preco))
if quantidade > 100:
    preco2=quantidade * fotocopia2
    print("O valor das cópias é: R$ {}" .format(preco2))

