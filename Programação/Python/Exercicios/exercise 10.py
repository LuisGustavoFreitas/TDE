#O IMC, índice de massa corporal, é calculado através da seguinte fórmula: IMC = massa /
#altura2
#Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do
#usuário e mostre o valor do IMC e qual sua condição segundo o critério apresentado na
#tabela da OMS (Organização Mundial de Saúde)

#Entrada
massa=float(input('Informe o peso:'))
altura=float(input('Informe a altura:'))

#Desenvolvimento
imc=massa/(altura**2)
if imc < 18.5:
    print('Abaixo do peso')
if imc >= 18.5 and imc < 25:
    print('Peso ideal')
if imc >= 25 and imc < 30:
    print('Sobrepeso')
if imc >= 30 and imc < 35:
    print('Obesidade')
if imc >= 35 and imc < 40:
    print('Obesidade grau 2')
