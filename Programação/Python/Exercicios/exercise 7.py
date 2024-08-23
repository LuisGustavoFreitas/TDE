#O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
#IMC = massa / altura2
#Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
#e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério
#apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. Caso
#não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9).

#Entrada
massa=float(input('Informe o peso em quilogramas:'))
altura=float(input('Informe a altura em metros:'))

#Desenvolvimento
imc=massa/(altura**2)
def calcular_peso_normal(altura):
    return 24.9 * (altura ** 2)
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

else:
    peso_normal = calcular_peso_normal(altura)
    print(f"Para sua altura, a massa máxima considerada normal seria de aproximadamente {peso_normal:.2f} quilogramas.")

