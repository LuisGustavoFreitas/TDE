#Entrada
massa=float(input('Informe o peso:'))
altura=float(input('Informe a altura:'))

#Desenvolvimento
imc=massa/(altura**2)
print('O seu  IMC é: {} '.format(imc))
if imc < 17:
    print('Abaixo do ideal')
if imc >= 17 and imc < 21:
    print('IMC ideal')
if imc >= 21 and imc < 26:
    print('IMC está acima do ideal')
if imc >= 26:
    print('IMC está muito acima do ideal')

