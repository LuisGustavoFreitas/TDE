#Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação
#segundo uma das seguintes categorias:

#Entrada
idade=int(input("Digite sua idade: "))

#Desenvolvimento
if idade>=5 and idade<= 7:
    print("Categoria Infantil A")
if idade>=8 and idade<=10:
    print("Categoria Infantil B")
if idade>=11 and idade<=13:
    print("Categoria Juvenil A")
if idade>=14 and idade<=17:
    print("Categoria Juvenil B")
if idade>=18:
    print("Categoria Adulto")
