#Leia dois valores reais do teclado, calcular e imprimir na tela:
# a) A soma destes valores b) O produto deles c) O quociente entre eles

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o primeiro número: '))

print("""
[1] - A soma entre eles;
[2] - O produto entre eles;
[3] - O quociente entre eles;
""")
opcao= int(input('Digite qual você deseja: '))
if opcao == 1:
    Sn = n1 + n2
    print(Sn)
elif opcao == 2: 
    Pn = n1 * n2
    print(Pn)
else:
    Qn = n1 / n2
    print(Qn)
